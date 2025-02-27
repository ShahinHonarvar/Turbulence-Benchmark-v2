from collections import defaultdict

def if_contains_anagrams(strings):

    def sorted_str(s):
        return ''.join(sorted(s.lower()))
    anagram_count = 0
    anagram_dict = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            key = sorted_str(s)
            anagram_dict[key] += 1
    for count in anagram_dict.values():
        anagram_count += count * (count - 1) // 2
        if anagram_count > 89:
            return False
    return True