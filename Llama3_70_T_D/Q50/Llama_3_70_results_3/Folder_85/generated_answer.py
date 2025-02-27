def if_contains_anagrams(lst):
    anagram_map = {}
    count = 0
    for word in lst:
        lower_word = word.lower()
        sorted_word = ''.join(sorted(lower_word))
        if sorted_word in anagram_map:
            anagram_map[sorted_word].append(lower_word)
        else:
            anagram_map[sorted_word] = [lower_word]
    for key in anagram_map:
        if len(anagram_map[key]) > 1 and len(key) >= 3:
            count += len(anagram_map[key]) * (len(anagram_map[key]) - 1) // 2
    return count >= 73