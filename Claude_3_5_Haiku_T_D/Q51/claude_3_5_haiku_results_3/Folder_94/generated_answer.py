def if_contains_anagrams(word_list):

    def is_anagram(word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower())

    def count_anagram_pairs(words):
        pairs = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if len(words[i]) >= 3 and len(words[j]) >= 3 and is_anagram(words[i], words[j]):
                    pairs += 1
        return pairs
    return count_anagram_pairs(word_list) <= 181