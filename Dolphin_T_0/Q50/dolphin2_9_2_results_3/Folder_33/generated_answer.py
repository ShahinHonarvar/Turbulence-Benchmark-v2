def if_contains_anagrams(lst):
    anagram_count = 0
    anagram_pairs = {}
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            if sorted_word in anagram_pairs:
                anagram_pairs[sorted_word] += 1
                anagram_count += 1
            else:
                anagram_pairs[sorted_word] = 1
    return anagram_count >= 140