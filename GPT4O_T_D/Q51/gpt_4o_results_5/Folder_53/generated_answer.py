def if_contains_anagrams(words):

    def canonical_form(word):
        return ''.join(sorted(word.lower()))

    def is_anagram(word1, word2):
        return canonical_form(word1) == canonical_form(word2) and len(word1) >= 3
    anagram_pairs = 0
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if is_anagram(words[i], words[j]):
                anagram_pairs += 1
                if anagram_pairs > 8:
                    return False
    return True