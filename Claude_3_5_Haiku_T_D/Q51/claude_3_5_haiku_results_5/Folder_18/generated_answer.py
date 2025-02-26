def if_contains_anagrams(word_list):

    def is_valid_anagram(word):
        return len(word) >= 3 and word.isalpha()

    def normalize_word(word):
        return ''.join(sorted(word.lower()))
    valid_normalized_words = [normalize_word(word) for word in word_list if is_valid_anagram(word)]
    anagram_count = sum((1 for i in range(len(valid_normalized_words)) for j in range(i + 1, len(valid_normalized_words)) if valid_normalized_words[i] == valid_normalized_words[j]))
    return anagram_count <= 42