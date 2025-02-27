def if_contains_anagrams(lst):
    anagrams = 0
    anagram_pairs = set()
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            if sorted_word in anagram_pairs:
                anagrams += 1
            else:
                anagram_pairs.add(sorted_word)
    return anagrams >= 8