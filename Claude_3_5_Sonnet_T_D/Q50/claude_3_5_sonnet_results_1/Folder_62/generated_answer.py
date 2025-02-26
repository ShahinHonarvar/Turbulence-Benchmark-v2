def if_contains_anagrams(string_list):
    anagram_count = 0
    processed_words = set()
    for i, word in enumerate(string_list):
        word = word.lower()
        if len(word) < 3 or word in processed_words:
            continue
        sorted_word = ''.join(sorted(word))
        processed_words.add(word)
        for other_word in string_list[i + 1:]:
            other_word = other_word.lower()
            if len(other_word) < 3:
                continue
            if ''.join(sorted(other_word)) == sorted_word:
                anagram_count += 1
                if anagram_count >= 43:
                    return True
    return False