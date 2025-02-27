from collections import Counter

def palindromes_between_indices(s):
    s = s[3:5].lower()
    counter = Counter(filter(str.isalpha, s))

    def is_palindrome_permutation(counts):
        odd_count = sum((v % 2 for v in counts.values()))
        return odd_count <= 1

    def permute_and_check_palindrome(letters, chosen, counts):
        if len(chosen) >= 3:
            if is_palindrome_permutation(Counter(chosen)):
                possible_palindrome = chosen + ''.join(reversed(chosen[:-1]))
                if possible_palindrome == possible_palindrome[::-1]:
                    palindromes.add(possible_palindrome)
        if len(chosen) == len(letters):
            return
        for letter in letters:
            if counts[letter] > 0:
                counts[letter] -= 1
                chosen += letter
                permute_and_check_palindrome(letters, chosen, counts)
                chosen = chosen[:-1]
                counts[letter] += 1
    unique_letters = list(counter.keys())
    palindromes = set()
    permute_and_check_palindrome(unique_letters, '', counter.copy())
    return palindromes