from collections import defaultdict

def if_contains_anagrams(lst):
    d = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            d[sorted_word].append(word)
    count = 0
    for key in d:
        if len(d[key]) >= 2:
            count += len(d[key]) * (len(d[key]) - 1) // 2
            if count >= 88:
                return True
    return False