from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_count = 0
    string_dict = defaultdict(list)
    for s in strings:
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s.lower()))
        string_dict[sorted_s].append(s)
    for key in string_dict:
        n = len(string_dict[key])
        if n > 1:
            anagram_count += n * (n - 1) // 2
    return anagram_count <= 84