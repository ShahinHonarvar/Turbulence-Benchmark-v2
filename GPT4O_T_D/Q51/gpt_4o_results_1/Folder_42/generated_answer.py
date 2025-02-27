from collections import defaultdict

def if_contains_anagrams(lst):

    def sorted_string(s):
        return ''.join(sorted(s.lower()))
    anagram_count = 0
    substrings = defaultdict(int)
    for word in lst:
        if len(word) >= 3:
            key = sorted_string(word)
            anagram_count += substrings[key]
            substrings[key] += 1
            if anagram_count > 38:
                return False
    return True