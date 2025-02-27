from itertools import permutations
    from collections import Counter

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    english_letters = ''.join([char.lower() for char in s[0:6] if char.isalpha()])
    count = Counter(english_letters)
    palindromes = set()
    half_palindrome_candidates = set([''.join(p) for p in permutations(english_letters) if len(p) >= 2])
    for candidate in half_palindrome_candidates:
        if len(candidate) % 2 == 0:
            word = candidate + candidate[::-1]
        else:
            for mid in count:
                if count[mid] % 2 == 1:
                    word = candidate + mid + candidate[::-1]
                    break
        if len(word) >= 4 and is_palindrome(word):
            palindromes.add(word)
    return palindromes