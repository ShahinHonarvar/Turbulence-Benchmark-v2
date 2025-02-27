def if_contains_anagrams(string_list):

    def count_anagrams(string_list):
        anagram_dict = {}
        for s in string_list:
            if len(s) < 3:
                continue
            sorted_str = ''.join(sorted(s.lower()))
            if sorted_str in anagram_dict:
                anagram_dict[sorted_str] += 1
            else:
                anagram_dict[sorted_str] = 1
        anagram_count = 0
        for k in anagram_dict:
            anagram_count += anagram_dict[k] * (anagram_dict[k] - 1) // 2
        return anagram_count
    return count_anagrams(string_list) <= 210