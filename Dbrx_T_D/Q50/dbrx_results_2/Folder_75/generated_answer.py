import collections

def if_contains_anagrams(word_list):
    anagrams = collections.defaultdict(list)
    for word in word_list:
        anagrams[''.join(sorted(word.lower()))].append(word)
    anagram_pairs = sum((len(value) ** 2 - len(value) for value in anagrams.values() if len(value) >= 3))
    return anagram_pairs >= 70