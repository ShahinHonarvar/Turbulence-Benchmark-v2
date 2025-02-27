from collections import defaultdict

def if_contains_anagrams(strings):

    def sorted_str(s):
        return ''.join(sorted(s.lower()))
    anagram_count = 0
    anagram_groups = defaultdict(int)
    for string in strings:
        if len(string) >= 3:
            sorted_string = sorted_str(string)
            anagram_count += anagram_groups[sorted_string]
            anagram_groups[sorted_string] += 1
            if anagram_count > 188:
                return False
    return True