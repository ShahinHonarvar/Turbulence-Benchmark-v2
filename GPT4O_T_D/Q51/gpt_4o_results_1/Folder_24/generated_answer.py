def if_contains_anagrams(words):

    def is_anagram(word1, word2):
        return sorted(word1) == sorted(word2)

    def preprocess(word):
        return ''.join(sorted(filter(str.isalpha, word.lower())))
    valid_words = [preprocess(word) for word in words if len(word) >= 3]
    pair_count = 0
    for i in range(len(valid_words)):
        for j in range(i + 1, len(valid_words)):
            if is_anagram(valid_words[i], valid_words[j]):
                pair_count += 1
                if pair_count > 96:
                    return False
    return True