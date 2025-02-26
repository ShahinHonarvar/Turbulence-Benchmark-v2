def if_contains_anagrams(string_list):
    anagram_count = 0
    processed = set()
    for i, word1 in enumerate(string_list):
        if len(word1) < 3 or word1.lower() in processed:
            continue
        sorted_word1 = ''.join(sorted(word1.lower()))
        for word2 in string_list[i + 1:]:
            if len(word2) < 3:
                continue
            if sorted_word1 == ''.join(sorted(word2.lower())) and word1.lower() != word2.lower():
                anagram_count += 1
                processed.add(word1.lower())
                processed.add(word2.lower())
                if anagram_count >= 18:
                    return True
                break
    return False