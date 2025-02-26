def if_contains_anagrams(words):

    def is_anagram(word1, word2):
        word1 = ''.join(sorted(word1.lower()))
        word2 = ''.join(sorted(word2.lower()))
        return word1 == word2
    anagram_pairs = 0
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if len(words[i]) >= 3 and len(words[j]) >= 3:
                if is_anagram(words[i], words[j]):
                    anagram_pairs += 1
    return anagram_pairs <= 98