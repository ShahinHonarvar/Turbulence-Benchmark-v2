def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(filter(str.isalpha, s.lower())))
    anagram_dict = {}
    count = 0
    for s in strings:
        if len(s) < 3:
            continue
        norm = normalize(s)
        if norm in anagram_dict:
            count += anagram_dict[norm]
            anagram_dict[norm] += 1
        else:
            anagram_dict[norm] = 1
        if count > 54:
            return False
    return True