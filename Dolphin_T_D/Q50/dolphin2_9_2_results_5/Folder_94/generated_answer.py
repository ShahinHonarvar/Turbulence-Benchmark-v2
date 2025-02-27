from collections import Counter

def if_contains_anagrams(lst):
    c = Counter()
    count = 0
    for word in lst:
        if len(word) >= 3:
            word_sorted = ''.join(sorted(word.lower()))
            c[word_sorted] += 1
    for key in c:
        if c[key] > 1 and c[key] * (c[key] - 1) // 2 >= 46:
            count += 1
    return count >= 46