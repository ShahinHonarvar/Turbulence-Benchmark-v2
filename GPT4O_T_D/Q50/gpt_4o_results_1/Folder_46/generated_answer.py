from collections import defaultdict

def if_contains_anagrams(strings):

    def sorted_lower(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = defaultdict(int)
    for string in strings:
        if len(string) >= 3:
            sorted_string = sorted_lower(string)
            anagram_dict[sorted_string] += 1
    anagram_pairs = 0
    for count in anagram_dict.values():
        if count > 1:
            anagram_pairs += count * (count - 1) // 2
            if anagram_pairs >= 38:
                return True
    return False