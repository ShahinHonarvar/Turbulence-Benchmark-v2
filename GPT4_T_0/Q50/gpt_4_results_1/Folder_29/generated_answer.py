from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagrams[sorted_word].append(word)
    count = sum((len(values) * (len(values) - 1) // 2 for values in anagrams.values()))
    return count >= 35