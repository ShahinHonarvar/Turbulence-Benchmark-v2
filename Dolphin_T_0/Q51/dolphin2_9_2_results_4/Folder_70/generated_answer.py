from collections import Counter

def if_contains_anagrams(lst):
    anagram_count = 0
    candidates = {(Counter(word.lower()), word.lower()): word for word in lst if len(set(word)) >= 3 and len(word.lower()) >= 3}
    for word1, word2 in zip(lst, lst[1:]):
        if Counter(word1.lower()) == Counter(word2.lower()) and word1.lower() != word2.lower():
            anagram_count += 1
            candidates.pop((Counter(word1.lower()), word1.lower()), None)
            candidates.pop((Counter(word2.lower()), word2.lower()), None)
    return anagram_count <= 97 and len(candidates) <= 2