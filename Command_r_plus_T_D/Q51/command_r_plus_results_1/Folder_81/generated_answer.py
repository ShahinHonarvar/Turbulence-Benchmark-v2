def if_contains_anagrams(lst):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_count = 0
    anagram_dict = {}
    for word in lst:
        if len(word) < 3:
            continue
        normalized = normalize(word)
        if normalized in anagram_dict:
            anagram_dict[normalized].append(word)
        else:
            anagram_dict[normalized] = [word]
    for anagram_list in anagram_dict.values():
        if len(anagram_list) > 1:
            anagram_count += len(anagram_list)
    return anagram_count <= 79