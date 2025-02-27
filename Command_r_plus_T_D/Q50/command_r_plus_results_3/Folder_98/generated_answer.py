def if_contains_anagrams(words_list: list[str]) -> bool:
    anagram_count = 0
    anagram_pairs = {}
    for word in words_list:
        sorted_word = ''.join(sorted(word.lower()))
        if sorted_word in anagram_pairs:
            anagram_pairs[sorted_word].append(word)
        else:
            anagram_pairs[sorted_word] = [word]
    for anagram_group in anagram_pairs.values():
        if len(anagram_group) >= 2 and len(anagram_group[0]) >= 3:
            anagram_count += 1
            if anagram_count >= 7:
                return True
    return False