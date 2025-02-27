from collections import defaultdict

def if_contains_anagrams(strings):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagram_count = 0
    anagram_map = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            norm = normalize(s)
            anagram_map[norm] += 1
    for count in anagram_map.values():
        if count > 1:
            anagram_count += count * (count - 1) // 2
            if anagram_count > 50:
                return False
    return True