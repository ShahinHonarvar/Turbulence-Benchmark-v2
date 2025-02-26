def if_contains_anagrams(string_list):
    anagram_count = 0
    processed_words = set()
    for i in range(len(string_list)):
        word = string_list[i].lower()
        if len(word) < 3 or word in processed_words:
            continue
        sorted_word = ''.join(sorted(word))
        processed_words.add(word)
        for j in range(i + 1, len(string_list)):
            compare_word = string_list[j].lower()
            if len(compare_word) < 3:
                continue
            if ''.join(sorted(compare_word)) == sorted_word:
                anagram_count += 1
                if anagram_count >= 67:
                    return True
    return False