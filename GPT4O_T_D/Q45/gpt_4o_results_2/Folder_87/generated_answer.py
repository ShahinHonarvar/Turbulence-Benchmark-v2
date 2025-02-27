from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    english_letters = [ch for ch in s[3:10].lower() if ch.isalpha()]
    result = set()
    if len(english_letters) >= 3:
        for i in range(3, len(english_letters) + 1):
            for perm in permutations(english_letters, i):
                candidate = ''.join(perm)
                if is_palindrome(candidate):
                    result.add(candidate)
    return result