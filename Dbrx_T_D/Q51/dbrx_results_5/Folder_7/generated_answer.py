import collections

def are_anagrams(word1, word2):
    return len(word1) == len(word2) and collections.Counter(word1.lower()) == collections.Counter(word2.lower())

def count_anagram_pairs(words):
    words = [word for word in words if len(word) >= 3]
    anagrams = collections.defaultdict(list)
    for word in words:
        anagrams[''.join(sorted(word.lower()))].append(word)
    return sum((len(pair) == 2 for pair in anagrams.values()))

def if_contains_anagrams(words):
    return count_anagram_pairs(words) <= 445