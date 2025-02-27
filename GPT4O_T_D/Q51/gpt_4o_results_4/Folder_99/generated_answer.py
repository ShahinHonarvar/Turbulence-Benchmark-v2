def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagram_count = 0
    normalized_words = [''.join(sorted(word.lower())) for word in words if len(word) >= 3]
    while normalized_words:
        current_word = normalized_words.pop()
        anagram_count += normalized_words.count(current_word)
        normalized_words = [word for word in normalized_words if word != current_word]
    return anagram_count <= 93