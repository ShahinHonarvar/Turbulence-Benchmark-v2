from collections import Counter
    from itertools import combinations, permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    sub_string = s[4:9].lower()
    letter_counts = Counter(filter(str.isalpha, sub_string))
    palindromes = set()
    for length in range(3, len(sub_string) + 1):
        for combination in combinations(letter_counts.elements(), length):
            for permutation in permutations(combination):
                word = ''.join(permutation)
                if is_palindrome(word):
                    palindromes.add(word)
    return palindromes