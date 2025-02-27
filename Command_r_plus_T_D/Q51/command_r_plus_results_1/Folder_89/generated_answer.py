def normalize_string(s):
    return ''.join((c for c in s.lower() if c.isalpha()))

def if_contains_anagrams(words_list):
    anagram_count = 0
    anagram_dict = {}
    for word in words_list:
        normalized_word = normalize_string(word)
        if len(normalized_word) < 3:
            continue
        if normalized_word in anagram_dict:
            anagram_dict[normalized_word].append(word)
        else:
            anagram_dict[normalized_word] = [word]
    for anagram_list in anagram_dict.values():
        if len(anagram_list) > 1:
            anagram_count += 1
    return anagram_count <= 73