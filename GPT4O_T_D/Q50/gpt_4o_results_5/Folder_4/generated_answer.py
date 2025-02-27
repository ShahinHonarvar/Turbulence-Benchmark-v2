from collections import defaultdict

def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_map = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            key = normalize(string)
            anagram_map[key].append(string)
    count = 0
    for anagram_list in anagram_map.values():
        n = len(anagram_list)
        if n > 1:
            count += n * (n - 1) // 2
            if count >= 42:
                return True
    return False