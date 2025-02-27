from collections import defaultdict

def if_contains_anagrams(strings):

    def sort_string(s):
        return ''.join(sorted(s))
    anagram_count = 0
    anagram_map = defaultdict(list)
    for s in strings:
        s = s.lower()
        if len(s) >= 3:
            sorted_s = sort_string(s)
            anagram_map[sorted_s].append(s)
    for words in anagram_map.values():
        count = len(words)
        if count > 1:
            anagram_count += count * (count - 1) // 2
            if anagram_count > 96:
                return False
    return True