def if_contains_anagrams(words_list):

    def normalize_text(text):
        return text.lower()

    def is_anagram(str1, str2):
        return sorted(str1) == sorted(str2)
    anagram_count = 0
    word_set = set()
    for word in words_list:
        normalized_word = normalize_text(word)
        if len(normalized_word) < 3:
            continue
        for existing_word in word_set:
            if is_anagram(normalized_word, existing_word):
                anagram_count += 1
                if anagram_count > 318:
                    return False
                break
        word_set.add(normalized_word)
    return True