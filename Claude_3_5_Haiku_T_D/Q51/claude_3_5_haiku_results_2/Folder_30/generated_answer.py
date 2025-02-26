def if_contains_anagrams(words):

    def normalize_word(word):
        return ''.join(sorted(word.lower()))
    anagram_count = 0
    normalized_words = {}
    for word in words:
        if len(word) < 3:
            continue
        normalized = normalize_word(word)
        if normalized in normalized_words:
            anagram_count += 1
            if anagram_count > 28:
                return False
            normalized_words[normalized] += 1
        else:
            normalized_words[normalized] = 1
    return True