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
            anagram_count += 1
            if anagram_count > 54:
                return False
        else:
            anagram_dict[normalized] = word
    return True