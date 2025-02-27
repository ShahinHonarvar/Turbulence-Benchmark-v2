from collections import defaultdict

def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    substr = s[5:9].lower()
    result = set()
    if len(substr) < 3:
        return result
    for i in range(len(substr) - 2):
        for j in range(i + 3, len(substr) + 1):
            candidate = substr[i:j]
            if set(candidate) <= english_letters and candidate == candidate[::-1]:
                result.add(candidate)
    return result