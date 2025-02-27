def if_contains_anagrams(lst):
    anagram_map = {}
    for word in lst:
        lower_word = word.lower()
        sorted_word = ''.join(sorted(lower_word))
        if len(lower_word) >= 3:
            if sorted_word in anagram_map:
                anagram_map[sorted_word].append(lower_word)
            else:
                anagram_map[sorted_word] = [lower_word]
    count = 0
    for value in anagram_map.values():
        count += len(value) * (len(value) - 1) // 2
    return count >= 25