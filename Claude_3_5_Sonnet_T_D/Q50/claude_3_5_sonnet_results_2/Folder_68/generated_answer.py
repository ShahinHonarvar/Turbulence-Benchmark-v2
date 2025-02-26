def if_contains_anagrams(string_list):
    anagram_count = 0
    processed = set()
    for i, word in enumerate(string_list):
        if len(word) < 3 or word.lower() in processed:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        for j in range(i + 1, len(string_list)):
            compare_word = string_list[j]
            if len(compare_word) < 3:
                continue
            if ''.join(sorted(compare_word.lower())) == sorted_word:
                anagram_count += 1
                if anagram_count >= 9:
                    return True
        processed.add(word.lower())
    return False