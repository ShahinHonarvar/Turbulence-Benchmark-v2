from collections import defaultdict

def if_contains_anagrams(strings):
    d = defaultdict(list)
    for word in strings:
        sorted_word = ''.join(sorted(word.lower()))
        if len(word) >= 3:
            d[sorted_word].append(word)
    count = 0
    for key in d:
        if len(d[key]) >= 2:
            count += len(d[key]) * (len(d[key]) - 1) // 2
    return count >= 91