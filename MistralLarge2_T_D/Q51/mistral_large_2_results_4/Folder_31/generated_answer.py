from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_count = 0
    string_dict = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            canonical_form = ''.join(sorted(string.lower()))
            string_dict[canonical_form].append(string)
    for anagrams in string_dict.values():
        if len(anagrams) > 1:
            pairs = len(anagrams) * (len(anagrams) - 1) // 2
            anagram_count += pairs
    return anagram_count <= 65