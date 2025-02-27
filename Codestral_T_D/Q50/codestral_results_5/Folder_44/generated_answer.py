def if_contains_anagrams(words):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_pairs = 0
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            word1, word2 = (words[i], words[j])
            if len(word1) >= 3 and len(word2) >= 3 and is_anagram(word1, word2):
                anagram_pairs += 1
    return anagram_pairs >= 44