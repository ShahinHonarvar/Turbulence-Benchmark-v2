from collections import defaultdict

def if_contains_anagrams(strings):

    def canonical_form(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            anagram_dict[canonical_form(s)].append(s)
    count = 0
    for anagram_list in anagram_dict.values():
        n = len(anagram_list)
        if n > 1:
            count += n * (n - 1) // 2
        if count >= 58:
            return True
    return False