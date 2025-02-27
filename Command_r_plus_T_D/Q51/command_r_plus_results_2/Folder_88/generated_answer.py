def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagram_count = 0
    anagram_dict = {}
    for word in words:
        if len(word) < 3:
            continue
        normalized_word = normalize(word)
        if normalized_word in anagram_dict:
            anagram_count += 1
            anagram_dict[normalized_word] += 1
        else:
            anagram_dict[normalized_word] = 1
    return anagram_count <= 407