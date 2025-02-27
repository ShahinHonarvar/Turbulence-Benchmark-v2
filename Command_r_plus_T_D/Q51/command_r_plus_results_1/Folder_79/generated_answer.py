def if_contains_anagrams(words_list):

    def normalize_text(word):
        return ''.join((e for e in word.lower() if e.isalpha()))

    def is_anagram(word1, word2):
        return sorted(word1) == sorted(word2)
    anagram_count = 0
    word_set = set(words_list)
    for word in word_set:
        normalized_word = normalize_text(word)
        if len(normalized_word) < 3:
            continue
        for other_word in word_set - {word}:
            other_normalized_word = normalize_text(other_word)
            if is_anagram(normalized_word, other_normalized_word):
                anagram_count += 1
                if anagram_count > 173:
                    return False
    return True