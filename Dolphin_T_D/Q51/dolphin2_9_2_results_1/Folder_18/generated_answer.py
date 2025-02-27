import itertools

def if_contains_anagrams(lst):
    anagrams_found = set()
    for word1 in lst:
        if len(word1) >= 3:
            for word2 in lst:
                if word1.lower() == word2.lower() and word1 != word2:
                    anagram_word = ''.join(sorted(word1.lower()))
                    if anagram_word not in anagrams_found:
                        anagram_pairs = list(itertools.combinations(lst, 2))
                        pairs_found = 0
                        for pair in anagram_pairs:
                            if len(pair[0]) >= 3 and len(pair[1]) >= 3 and (sorted(pair[0].lower()) == sorted(pair[1].lower())):
                                pairs_found += 1
                        if pairs_found >= 42:
                            return True
                    anagrams_found.add(anagram_word)
    return False