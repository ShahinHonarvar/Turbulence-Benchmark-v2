def if_contains_anagrams(strings):

    def sorted_string(s):
        return ''.join(sorted(s))
    count = 0
    lowered_strings = [s.lower() for s in strings]
    length_filtered_strings = [s for s in lowered_strings if len(s) >= 3]
    anagram_dict = {}
    for string in length_filtered_strings:
        sorted_str = sorted_string(string)
        if sorted_str in anagram_dict:
            anagram_dict[sorted_str] += 1
        else:
            anagram_dict[sorted_str] = 1
    for key, value in anagram_dict.items():
        if value > 1:
            count += value * (value - 1) // 2
    return count <= 91