def if_contains_anagrams(words):

    def is_anagram(word1, word2):
        return len(word1) >= 3 and len(word2) >= 3 and (sorted(word1.lower()) == sorted(word2.lower()))
    anagram_count = 0
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if is_anagram(words[i], words[j]):
                anagram_count += 1
    return anagram_count <= 35