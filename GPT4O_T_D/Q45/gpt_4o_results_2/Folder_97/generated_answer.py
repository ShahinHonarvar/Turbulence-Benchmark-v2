from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    s = s.lower()
    substr = ''.join(filter(str.isalpha, s[:5]))
    palindromes = set()
    for length in range(3, len(substr) + 1):
        for p in permutations(substr, length):
            p_str = ''.join(p)
            if is_palindrome(p_str):
                palindromes.add(p_str)
    return palindromes