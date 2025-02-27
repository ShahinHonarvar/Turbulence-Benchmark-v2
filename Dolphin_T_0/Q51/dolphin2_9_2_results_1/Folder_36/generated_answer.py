from collections import Counter

def if_contains_anagrams(strings_list):
    counter = Counter()
    for word in strings_list:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            counter[sorted_word] += 1
    res = sum((value >= 2 for value in counter.values()))
    return res <= 25