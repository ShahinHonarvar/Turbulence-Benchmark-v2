from collections import defaultdict

def if_contains_anagrams(words):
    count = 0
    d = defaultdict(list)
    for word in words:
        key = ''.join(sorted(word.lower()))
        if len(key) >= 3:
            d[key].append(word)
    for key in d:
        if len(d[key]) >= 2:
            count += len(d[key]) * (len(d[key]) - 1) // 2
    return count >= 98