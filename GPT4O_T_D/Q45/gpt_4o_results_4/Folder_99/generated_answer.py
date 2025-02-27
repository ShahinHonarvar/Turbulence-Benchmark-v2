from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    s = s.lower()
    sub_str = s[4:9]
    english_letters = ''.join([c for c in sub_str if c.isalpha()])
    palindromes = set()
    for length in range(3, len(english_letters) + 1):
        for perm in permutations(english_letters, length):
            word = ''.join(perm)
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes