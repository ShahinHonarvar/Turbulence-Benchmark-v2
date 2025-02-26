def if_contains_anagrams(words):

    def is_valid_word(word):
        return len(word) >= 3 and word.isalpha()

    def normalize_word(word):
        return ''.join(sorted(word.lower()))
    valid_words = [word for word in words if is_valid_word(word)]
    word_signatures = [normalize_word(word) for word in valid_words]
    anagram_pairs = 0
    for i in range(len(word_signatures)):
        for j in range(i + 1, len(word_signatures)):
            if word_signatures[i] == word_signatures[j]:
                anagram_pairs += 1
                if anagram_pairs > 48:
                    return False
    return True