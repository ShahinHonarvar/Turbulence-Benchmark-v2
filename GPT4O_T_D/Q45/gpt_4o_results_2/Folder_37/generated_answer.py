from itertools import permutations

def palindromes_between_indices(s: str) -> set:

    def is_palindrome(word):
        return word == word[::-1]
    sub_str = ''.join(filter(str.isalpha, s[1:5])).lower()
    palindromes = set()
    for length in range(5, len(sub_str) + 1):
        for perm in permutations(sub_str, length):
            candidate = ''.join(perm)
            if is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes