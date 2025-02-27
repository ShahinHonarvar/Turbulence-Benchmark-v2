import collections

def if_contains_anagrams(lst):
    anagrams = []
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            anagrams.append(sorted_word)
    anagram_counts = collections.Counter(anagrams)
    if len(anagram_counts) <= 30:
        return True
    else:
        return False