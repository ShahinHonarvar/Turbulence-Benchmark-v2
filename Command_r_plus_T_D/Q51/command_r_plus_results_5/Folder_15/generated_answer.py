def if_contains_anagrams(words):

    def normalize_text(text):
        return text.lower().replace(' ', '')

    def is_anagram(word1, word2):
        return sorted(word1) == sorted(word2)
    anagram_pairs = set()
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if len(words[i]) >= 3 and len(words[j]) >= 3:
                normalized_word1 = normalize_text(words[i])
                normalized_word2 = normalize_text(words[j])
                if is_anagram(normalized_word1, normalized_word2):
                    anagram_pairs.add(frozenset([words[i], words[j]]))
            if len(anagram_pairs) > 20:
                return False
    return True