import re
    from collections import defaultdict

def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]
    english_letters = set(re.findall('[a-zA-Z]', s[0:5]))
    palindromes = set()
    for length in range(3, 6):
        for char in english_letters:
            words = [''.join(word) for word in itertools.product(char, repeat=length)]
            palindromes.update(filter(is_palindrome, words))
    return palindromes