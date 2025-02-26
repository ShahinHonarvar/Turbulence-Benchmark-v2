def if_contains_anagrams(string_list):
    anagram_count = 0
    processed = set()
    for i, word in enumerate(string_list):
        if len(word) < 3 or word.lower() in processed:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        for other_word in string_list[i + 1:]:
            if len(other_word) < 3:
                continue
            if ''.join(sorted(other_word.lower())) == sorted_word:
                anagram_count += 1
                processed.add(word.lower())
                processed.add(other_word.lower())
                if anagram_count >= 28:
                    return True
    return False