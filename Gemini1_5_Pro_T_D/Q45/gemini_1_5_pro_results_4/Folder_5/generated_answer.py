from collections import Counter

def palindromes_between_indices(string):
    string = string[4:9].lower()
    letters = [letter for letter in string if letter.isalpha()]
    cnt = Counter(letters)
    odd_counts = [letter for letter, count in cnt.items() if count % 2 == 1]
    if len(odd_counts) > 1 or len(letters) < 4:
        return set()
    palindrome_half = ''.join([letter * (count // 2) for letter, count in cnt.items()])
    permutations = set()

    def generate_permutations(current_permutation):
        if len(current_permutation) == len(palindrome_half):
            permutations.add(current_permutation)
            return
        for letter in cnt:
            if cnt[letter] > 0:
                cnt[letter] -= 1
                generate_permutations(current_permutation + letter)
                cnt[letter] += 1
    generate_permutations('')
    return set([permutation + permutation[::-1] for permutation in permutations])