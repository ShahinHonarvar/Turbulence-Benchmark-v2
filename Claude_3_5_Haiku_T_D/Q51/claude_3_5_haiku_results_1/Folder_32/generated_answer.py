def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted(word.lower()))

    def is_valid_word(word):
        return len(word) >= 3 and word.isalpha()
    valid_words = [word for word in words if is_valid_word(word)]
    normalized_words = [normalize(word) for word in valid_words]
    anagram_pairs = 0
    for i in range(len(normalized_words)):
        for j in range(i + 1, len(normalized_words)):
            if normalized_words[i] == normalized_words[j]:
                anagram_pairs += 1
                if anagram_pairs > 89:
                    return False
    return True