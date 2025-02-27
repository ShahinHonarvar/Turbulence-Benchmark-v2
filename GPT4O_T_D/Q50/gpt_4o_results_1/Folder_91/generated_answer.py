def if_contains_anagrams(strings):

    def sort_string(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = {}
    for s in strings:
        if len(s) >= 3:
            sorted_s = sort_string(s)
            if sorted_s in anagram_dict:
                anagram_dict[sorted_s] += 1
            else:
                anagram_dict[sorted_s] = 1
    anagram_pairs = 0
    for count in anagram_dict.values():
        anagram_pairs += count * (count - 1) // 2
        if anagram_pairs >= 6:
            return True
    return False