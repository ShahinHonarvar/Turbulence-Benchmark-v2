def if_contains_anagrams(words):
    anagram_map = {}
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            if sorted_word in anagram_map:
                anagram_map[sorted_word] += 1
            else:
                anagram_map[sorted_word] = 1
    anagram_pair_count = sum((val * (val - 1) // 2 for val in anagram_map.values()))
    return anagram_pair_count >= 92