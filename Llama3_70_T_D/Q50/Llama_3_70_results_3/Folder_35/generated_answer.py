def if_contains_anagrams(lst):
    anagram_count = {}
    anagram_pairs = set()
    for word in lst:
        word_lower = word.lower()
        if len(word_lower) >= 3:
            sorted_word = ''.join(sorted(word_lower))
            if sorted_word in anagram_count:
                for pair in anagram_count[sorted_word]:
                    anagram_pairs.add(tuple(sorted([word_lower, pair])))
                anagram_count[sorted_word].append(word_lower)
            else:
                anagram_count[sorted_word] = [word_lower]
    return len(anagram_pairs) >= 153