def if_contains_anagrams(words):

    def normalize_word(word):
        return ''.join(sorted(word.lower()))
    anagram_pairs = 0
    seen_words = {}
    for word in words:
        if len(word) >= 3:
            normalized = normalize_word(word)
            if normalized in seen_words:
                anagram_pairs += 1
                if anagram_pairs > 86:
                    return False
                seen_words[normalized] += 1
            else:
                seen_words[normalized] = 1
    return True