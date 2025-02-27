from collections import defaultdict

def if_contains_anagrams(lst):
    count = 0
    anagrams = defaultdict(list)
    for word in lst:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        anagrams[sorted_word].append(word)
    for words in anagrams.values():
        if len(words) > 1:
            count += len(words) * (len(words) - 1) // 2
    return count <= 84