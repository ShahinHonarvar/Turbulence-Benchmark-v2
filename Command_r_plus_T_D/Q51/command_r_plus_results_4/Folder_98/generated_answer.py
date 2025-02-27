def if_contains_anagrams(words_list):

    def normalize_text(text):
        return text.lower()

    def sort_text(text):
        return ''.join(sorted(text))
    normalized_words = [normalize_text(word) for word in words_list]
    sorted_words = [sort_text(word) for word in normalized_words]
    anagram_count = 0
    for i in range(len(sorted_words)):
        for j in range(i + 1, len(sorted_words)):
            if sorted_words[i] == sorted_words[j] and len(words_list[i]) >= 3 and (len(words_list[j]) >= 3):
                anagram_count += 1
                if anagram_count > 46:
                    return False
    return True