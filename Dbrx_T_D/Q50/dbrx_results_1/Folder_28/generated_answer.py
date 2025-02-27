import collections

def if_contains_anagrams(lst):
    anagrams = collections.defaultdict(list)
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            anagrams[sorted_word].append(word)
    return len([words for words in anagrams.values() if len(words) >= 81]) > 0