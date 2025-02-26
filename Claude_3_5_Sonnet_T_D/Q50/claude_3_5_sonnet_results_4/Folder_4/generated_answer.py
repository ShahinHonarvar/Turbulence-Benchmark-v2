def if_contains_anagrams(string_list):
    anagram_count = 0
    processed = set()
    for i, word1 in enumerate(string_list):
        if len(word1) < 3:
            continue
        word1 = word1.lower()
        sorted_word1 = ''.join(sorted(word1))
        if sorted_word1 in processed:
            continue
        processed.add(sorted_word1)
        for word2 in string_list[i + 1:]:
            if len(word2) < 3:
                continue
            word2 = word2.lower()
            if sorted_word1 == ''.join(sorted(word2)) and word1 != word2:
                anagram_count += 1
                if anagram_count >= 42:
                    return True
    return False