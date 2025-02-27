from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    d = {}
    for word in lst:
        word = word.lower()
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word))
        if sorted_word not in d:
            d[sorted_word] = 0
        d[sorted_word] += 1
    for val in d.values():
        count += val * (val - 1) // 2
    return count <= 73