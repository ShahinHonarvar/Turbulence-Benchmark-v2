def if_contains_anagrams(words):

    def is_anagram(word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower())
    filtered_words = [word for word in words if len(word) >= 3]
    anagram_pairs_count = 0
    for i in range(len(filtered_words)):
        for j in range(i + 1, len(filtered_words)):
            if is_anagram(filtered_words[i], filtered_words[j]):
                anagram_pairs_count += 1
                if anagram_pairs_count > 75:
                    return False
    return True