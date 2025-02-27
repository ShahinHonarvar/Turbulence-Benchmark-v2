def if_contains_anagrams(strings):

    def sorted_chars(s):
        return ''.join(sorted((c for c in s.lower() if c.isalpha())))
    anagram_dict = {}
    for s in strings:
        if len(s) < 3:
            continue
        key = sorted_chars(s)
        if key in anagram_dict:
            anagram_dict[key].append(s)
        else:
            anagram_dict[key] = [s]
    anagram_pairs = 0
    for key, group in anagram_dict.items():
        count = len(group)
        if count > 1:
            anagram_pairs += count * (count - 1) // 2
            if anagram_pairs > 79:
                return False
    return True