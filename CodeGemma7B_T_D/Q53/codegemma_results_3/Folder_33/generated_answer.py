from collections import defaultdict
import string

def palindrome_of_length_at_least_n(s):
    """
    Write a function called 'palindrome_of_length_at_least_n' that takes one argument, a string, and returns the set of all palindromes of the length greater than or equal to 141 that exist in the given string. Each palindrome should only consist of English letters. If no such palindromes exist in the given string, the function should return an empty set. The function should find the palindromes in a case-insensitive manner.
    """
    letters = string.ascii_letters
    seen = defaultdict(int)
    for c in s.lower():
        if c in letters:
            seen[c] += 1

    def is_palindrome(word):
        a, b = (0, len(word) - 1)
        while a <= b:
            if word[a] != word[b]:
                return False
            a += 1
            b -= 1
        return True
    candidates = []
    for k, v in seen.items():
        for i in range(v - 140):
            candidates.append(k * (i + 141))
    result = set()
    for w in candidates:
        if is_palindrome(w):
            result.add(w)
    return result