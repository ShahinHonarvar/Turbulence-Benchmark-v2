from collections import defaultdict

def if_contains_anagrams(strings):

    def canonical_form(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = defaultdict(int)
    count = 0
    for string in strings:
        if len(string) >= 3:
            form = canonical_form(string)
            anagram_dict[form] += 1
    for key in anagram_dict:
        count += anagram_dict[key] * (anagram_dict[key] - 1) // 2
        if count > 24:
            return False
    return True