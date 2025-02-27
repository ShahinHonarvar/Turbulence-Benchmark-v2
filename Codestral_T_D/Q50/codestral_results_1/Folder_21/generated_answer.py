from collections import defaultdict

def if_contains_anagrams(lst):
    d = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            d[sorted_word].append(word.lower())
    count = 0
    for k, v in d.items():
        if len(v) >= 2:
            count += len(v) * (len(v) - 1) // 2
        if count >= 136:
            return True
    return False