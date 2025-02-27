def if_contains_anagrams(strings):

    def sorted_string(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = {}
    count = 0
    for s in strings:
        if len(s) >= 3:
            sorted_s = sorted_string(s)
            if sorted_s in anagram_dict:
                anagram_dict[sorted_s] += 1
            else:
                anagram_dict[sorted_s] = 1
    for value in anagram_dict.values():
        count += value * (value - 1) // 2
        if count >= 5:
            return True
    return False