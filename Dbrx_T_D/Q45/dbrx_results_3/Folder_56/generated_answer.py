from collections import defaultdict

def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    start, end = (5, 9)
    s = s.lower()
    if len(s) <= end or not english_letters.intersection(s[start:end + 1]):
        return set()
    palindromes = set()
    for i in range(start, end + 1):
        for j in range(i, end + 1):
            sub_s = s[i:j + 1]
            if english_letters.intersection(sub_s):
                if sub_s == sub_s[::-1]:
                    palindromes.add(sub_s)
    return {p for p in palindromes if len(p) >= 5}