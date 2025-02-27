def if_contains_anagrams(words):

    def sorted_word(word):
        return ''.join(sorted(word.lower()))

    def is_valid_anagram(word1, word2):
        return sorted_word(word1) == sorted_word(word2) and len(word1) >= 3 and (len(word2) >= 3)
    anagram_pairs = set()
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if is_valid_anagram(words[i], words[j]):
                anagram_pairs.add((min(words[i].lower(), words[j].lower()), max(words[i].lower(), words[j].lower())))
    return len(anagram_pairs) >= 4