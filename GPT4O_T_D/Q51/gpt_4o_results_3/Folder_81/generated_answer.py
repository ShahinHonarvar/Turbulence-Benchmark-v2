from collections import defaultdict

def if_contains_anagrams(strings):

    def canonical_form(s):
        return ''.join(sorted(s.lower()))
    anagram_map = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            form = canonical_form(string)
            anagram_map[form].append(string)
    anagram_count = 0
    for group in anagram_map.values():
        n = len(group)
        if n > 1:
            anagram_count += n * (n - 1) // 2
            if anagram_count > 79:
                return False
    return True