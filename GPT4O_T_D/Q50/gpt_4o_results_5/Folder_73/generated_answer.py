from collections import defaultdict

def if_contains_anagrams(strings):

    def sorted_string(s):
        return ''.join(sorted(s.lower()))
    valid_anagrams = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            sorted_s = sorted_string(s)
            valid_anagrams[sorted_s].append(s)
    anagram_pairs = 0
    for anagram_list in valid_anagrams.values():
        count = len(anagram_list)
        if count > 1:
            anagram_pairs += count * (count - 1) // 2
            if anagram_pairs >= 91:
                return True
    return False