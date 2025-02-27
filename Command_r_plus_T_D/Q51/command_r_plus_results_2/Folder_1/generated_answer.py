def if_contains_anagrams(words):

    def normalize_word(word):
        return ''.join(sorted(word.lower()))
    anagram_count = 0
    anagram_dict = {}
    for word in words:
        if len(word) < 3:
            continue
        normalized_word = normalize_word(word)
        if normalized_word in anagram_dict:
            anagram_count += 1
            anagram_dict[normalized_word].append(word)
        else:
            anagram_dict[normalized_word] = [word]
    return anagram_count <= 30