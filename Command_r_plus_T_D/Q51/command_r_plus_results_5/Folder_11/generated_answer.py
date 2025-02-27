def if_contains_anagrams(words_list):

    def normalize_text(word):
        return ''.join((e for e in word if e.isalpha())).lower()
    anagram_count = 0
    normalized_words = [normalize_text(word) for word in words_list]
    for i in range(len(normalized_words)):
        for j in range(i + 1, len(normalized_words)):
            if len(normalized_words[i]) >= 3 and len(normalized_words[j]) >= 3:
                if sorted(normalized_words[i]) == sorted(normalized_words[j]):
                    anagram_count += 1
                    if anagram_count > 41:
                        return False
    return True