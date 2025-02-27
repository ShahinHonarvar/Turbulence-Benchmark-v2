def if_contains_anagrams(lst):
    d = {}
    for word in lst:
        word_sorted = ''.join(sorted(word.lower()))
        d[word_sorted] = d.get(word_sorted, 0) + 1
    return sum((i * (i - 1) // 2 for i in d.values() if len(word_sorted) >= 3)) <= 407