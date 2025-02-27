def if_contains_anagrams(words):

    def normalize_word(word):
        return ''.join(sorted(word.lower()))
    normalized_words = [normalize_word(word) for word in words]
    anagram_pairs = 0
    for i in range(len(normalized_words)):
        for j in range(i + 1, len(normalized_words)):
            if normalized_words[i] == normalized_words[j] and len(words[i]) >= 3 and (len(words[j]) >= 3):
                anagram_pairs += 1
                if anagram_pairs > 54:
                    return False
    return True