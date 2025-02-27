from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(str_):
        return str_ == str_[::-1]
    if len(s) < 10:
        return set()
    substr = s[1:10].lower()
    english_letters = ''.join(filter(str.isalpha, substr))
    if len(english_letters) < 7:
        return set()
    palindromes = set()
    for length in range(7, len(english_letters) + 1):
        for perm in permutations(english_letters, length):
            perm_str = ''.join(perm)
            if is_palindrome(perm_str):
                palindromes.add(perm_str)
    return palindromes