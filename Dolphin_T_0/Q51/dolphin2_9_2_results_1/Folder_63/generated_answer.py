from collections import Counter

def if_contains_anagrams(s):
    c = Counter()
    for word in s:
        word = word.lower()
        if len(word) >= 3:
            c += Counter(word)
    count = 0
    for key in c:
        if c[key] % 2 == 0:
            count += c[key] // 2
    return count <= 423