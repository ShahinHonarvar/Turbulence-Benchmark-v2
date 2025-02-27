from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 10:
        return set()
    substring = s[8:10].lower()

    def is_palindrome(word):
        return word == word[::-1]
    letter_counts = Counter(filter(str.isalpha, substring))
    letters = ''.join((letter * (count // 2) for letter, count in letter_counts.items()))
    palindromes = set()
    for length in range(3, len(substring) + 1):
        for perm in permutations(letters, length // 2):
            half = ''.join(perm)
            if length % 2 == 0:
                candidate = half + half[::-1]
            else:
                for mid in letter_counts:
                    if letter_counts[mid] % 2 == 1:
                        candidate = half + mid + half[::-1]
                        if is_palindrome(candidate):
                            palindromes.add(candidate)
                        break
            if is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes