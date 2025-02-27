def if_contains_anagrams(lst):

    def normalize_string(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = {}
    for word in lst:
        normalized_word = normalize_string(word)
        if len(word) >= 3 and normalized_word not in anagram_dict:
            anagram_dict[normalized_word] = [word]
        elif len(word) >= 3 and normalized_word in anagram_dict:
            anagram_dict[normalized_word].append(word)
    anagram_pairs = sum((1 for words in anagram_dict.values() if len(words) > 1))
    return anagram_pairs <= 20