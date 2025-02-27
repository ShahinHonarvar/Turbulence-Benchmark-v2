from collections import defaultdict

def if_contains_anagrams(strings):

    def sorted_str(s):
        return ''.join(sorted(s.lower()))
    anagram_groups = defaultdict(int)
    for string in strings:
        if len(string) >= 3:
            anagram_groups[sorted_str(string)] += 1
    anagram_pairs = 0
    for count in anagram_groups.values():
        if count > 1:
            anagram_pairs += count * (count - 1) // 2
            if anagram_pairs >= 68:
                return True
    return anagram_pairs >= 68