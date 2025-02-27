def if_contains_anagrams(lst):

    def sorted_str(s):
        return ''.join(sorted(s.lower()))
    anagram_count = 0
    anagram_dict = {}
    for string in lst:
        if len(string) >= 3:
            key = sorted_str(string)
            if key in anagram_dict:
                anagram_count += anagram_dict[key]
                anagram_dict[key] += 1
            else:
                anagram_dict[key] = 1
            if anagram_count >= 97:
                return True
    return False