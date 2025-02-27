from collections import defaultdict

def if_contains_anagrams(words):
    anagrams = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagrams[sorted_word].append(word)
    count = sum([len(lst) * (len(lst) - 1) // 2 for lst in anagrams.values() if len(lst) > 1])
    return count >= 20