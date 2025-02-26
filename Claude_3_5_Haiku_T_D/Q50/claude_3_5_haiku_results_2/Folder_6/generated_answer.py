def if_contains_anagrams(words):

    def are_anagrams(word1, word2):
        return len(word1) >= 3 and len(word2) >= 3 and (sorted(word1.lower()) == sorted(word2.lower()))
    count_anagram_pairs = 0
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if are_anagrams(words[i], words[j]):
                count_anagram_pairs += 1
                if count_anagram_pairs >= 26:
                    return True
    return False