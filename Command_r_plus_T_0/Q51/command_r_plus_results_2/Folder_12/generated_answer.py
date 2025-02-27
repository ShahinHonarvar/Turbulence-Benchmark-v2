def if_contains_anagrams(lst):

    def normalize_text(text):
        return ''.join((e for e in text if e.isalpha())).lower()
    anagram_count = 0
    anagram_dict = {}
    for word in lst:
        normalized_word = normalize_text(word)
        if len(normalized_word) < 3:
            continue
        sorted_word = ''.join(sorted(normalized_word))
        if sorted_word in anagram_dict:
            anagram_dict[sorted_word].append(word)
        else:
            anagram_dict[sorted_word] = [word]
    for anagram_group in anagram_dict.values():
        if len(anagram_group) > 1:
            anagram_count += 1
    return anagram_count <= 92