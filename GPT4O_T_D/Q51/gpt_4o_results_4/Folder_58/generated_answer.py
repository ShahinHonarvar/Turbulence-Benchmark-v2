from collections import defaultdict

def if_contains_anagrams(strings):

    def sorted_str(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = defaultdict(list)
    for string in strings:
        clean_string = ''.join(filter(str.isalpha, string))
        if len(clean_string) >= 3:
            sorted_string = sorted_str(clean_string)
            anagram_dict[sorted_string].append(clean_string)
    anagram_pairs = 0
    for anagram_group in anagram_dict.values():
        count = len(anagram_group)
        if count > 1:
            anagram_pairs += count * (count - 1) // 2
            if anagram_pairs > 60:
                return False
    return True