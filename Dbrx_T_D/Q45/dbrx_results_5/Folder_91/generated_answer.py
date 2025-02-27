from collections import defaultdict
import string

def palindromes_between_indices(s):
    english_letters = set(string.ascii_lowercase + string.ascii_uppercase)
    letters_in_range = {c for i, c in enumerate(s.lower()) if 2 <= i <= 6}
    intersect = letters_in_range & english_letters
    if len(intersect) < 3:
        return set()
    result = set()
    for i in range(len(s) - 2):
        for j in range(i + 1, len(s)):
            if s[i] == s[j] and 2 <= i <= 6 and (2 <= j <= 6):
                pal = s[i:j + 1]
                if pal == pal[::-1]:
                    result.add(pal)
    for i in range(len(s) - 2, len(s)):
        for j in range(i - 1, -1, -1):
            if s[i] == s[j] and 2 <= i <= 6 and (2 <= j <= 6):
                pal = s[i:j:-1]
                if pal == pal[::-1]:
                    result.add(pal)
    return result