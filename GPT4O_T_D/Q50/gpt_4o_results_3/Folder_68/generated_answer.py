def if_contains_anagrams(strings):

    def sorted_str(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = {}
    count = 0
    for string in strings:
        if len(string) >= 3:
            sorted_s = sorted_str(string)
            if sorted_s in anagram_dict:
                anagram_dict[sorted_s] += 1
            else:
                anagram_dict[sorted_s] = 1
    for occurrences in anagram_dict.values():
        if occurrences > 1:
            count += occurrences * (occurrences - 1) // 2
            if count >= 9:
                return True
    return False