from itertools import permutations

def palindromes_between_indices(s):
    sub_string = s[2:7].lower()
    letters_only = ''.join(filter(str.isalpha, sub_string))
    palindromes = set()

    def is_palindrome(word):
        return word == word[::-1]
    for length in range(4, len(letters_only) + 1):
        for perm in set(permutations(letters_only, length)):
            candidate = ''.join(perm)
            if is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes