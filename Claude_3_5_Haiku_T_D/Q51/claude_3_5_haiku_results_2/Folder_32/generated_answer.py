def if_contains_anagrams(words):

    def is_anagram(word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower())

    def is_valid_length(word):
        return len(word) >= 3
    valid_words = [word for word in words if is_valid_length(word)]
    anagram_count = 0
    for i in range(len(valid_words)):
        for j in range(i + 1, len(valid_words)):
            if is_anagram(valid_words[i], valid_words[j]):
                anagram_count += 1
                if anagram_count > 89:
                    return False
    return True