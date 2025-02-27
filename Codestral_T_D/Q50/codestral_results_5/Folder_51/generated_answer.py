from collections import defaultdict

def if_contains_anagrams(lst):
    d = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            d[sorted_word].append(word)
    count = sum((len(anagrams) * (len(anagrams) - 1) // 2 for anagrams in d.values() if len(anagrams) >= 2))
    return count >= 39