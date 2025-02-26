def if_contains_anagrams(words):

    def is_anagram(word1, word2):
        return len(word1) >= 3 and len(word2) >= 3 and (sorted(word1.lower()) == sorted(word2.lower()))
    anagram_pairs = 0
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if is_anagram(words[i], words[j]):
                anagram_pairs += 1
                if anagram_pairs >= 29:
                    return True
    return False