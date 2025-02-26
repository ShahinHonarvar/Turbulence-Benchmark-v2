def if_contains_anagrams(words):

    def is_anagram(word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower())
    count_anagram_pairs = 0
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if len(words[i]) >= 3 and len(words[j]) >= 3:
                if is_anagram(words[i], words[j]):
                    count_anagram_pairs += 1
                    if count_anagram_pairs > 30:
                        return False
    return True