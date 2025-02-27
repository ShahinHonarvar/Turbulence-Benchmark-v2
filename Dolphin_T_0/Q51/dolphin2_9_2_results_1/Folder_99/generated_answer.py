from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    d = {}
    for word in lst:
        word_low = word.lower()
        word_sort = ''.join(sorted(word_low))
        d[word_sort] = d.get(word_sort, 0) + 1
        if d[word_sort] == 2:
            count += 1
    return count // 2 <= 93