def if_contains_anagrams(words_list):

    def normalize_text(word):
        return ''.join(filter(str.isalpha, word)).lower()

    def is_anagram(word1, word2):
        return sorted(word1) == sorted(word2)
    anagram_count = 0
    word_set = set()
    for word in words_list:
        normalized_word = normalize_text(word)
        if len(normalized_word) < 3:
            continue
        for other_word in word_set:
            if is_anagram(normalized_word, other_word):
                anagram_count += 1
                if anagram_count > 474:
                    return False
                break
        word_set.add(normalized_word)
    return True