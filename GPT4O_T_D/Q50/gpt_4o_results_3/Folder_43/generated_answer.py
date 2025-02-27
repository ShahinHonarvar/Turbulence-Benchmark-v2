from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagrams[sorted_word].append(word)
    count = 0
    for words in anagrams.values():
        if len(words) > 1:
            pairs = len(words) * (len(words) - 1) // 2
            count += pairs
            if count >= 61:
                return True
    return False