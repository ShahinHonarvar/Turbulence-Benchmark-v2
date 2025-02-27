import collections

def if_contains_anagrams(word_list):
    anagrams = collections.defaultdict(list)
    for word in word_list:
        anagrams[''.join(sorted(word.lower()))].append(word)
    anagram_counts = [len(group) for group in anagrams.values()]
    return sum(anagram_counts) > 15