from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    s = s[1:8].lower()
    valid_chars = ''.join(filter(str.isalpha, s))
    if len(valid_chars) < 6:
        return set()
    found_palindromes = set()
    for length in range(6, len(valid_chars) + 1):
        for p in permutations(valid_chars, length):
            p_word = ''.join(p)
            if is_palindrome(p_word):
                found_palindromes.add(p_word)
    return found_palindromes