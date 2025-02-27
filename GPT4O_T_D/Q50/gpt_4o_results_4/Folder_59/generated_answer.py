def if_contains_anagrams(strings):

    def sorted_string(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = {}
    pairs = 0
    for string in strings:
        if len(string) < 3:
            continue
        key = sorted_string(string)
        if key in anagram_dict:
            pairs += anagram_dict[key]
            anagram_dict[key] += 1
        else:
            anagram_dict[key] = 1
        if pairs >= 10:
            return True
    return False