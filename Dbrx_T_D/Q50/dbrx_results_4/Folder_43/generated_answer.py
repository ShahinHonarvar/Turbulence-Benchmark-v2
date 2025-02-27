import string

def if_contains_anagrams(lst):
    anagrams = []
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            anagrams.append(sorted_word)
    anagram_pairs = [anagrams.count(elem) - 1 for elem in set(anagrams) if anagrams.count(elem) > 1]
    return sum(anagram_pairs) >= 61