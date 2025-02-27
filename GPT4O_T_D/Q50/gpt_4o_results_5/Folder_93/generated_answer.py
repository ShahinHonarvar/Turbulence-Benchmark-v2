from collections import defaultdict

def if_contains_anagrams(strings):

    def sorted_form(s):
        return ''.join(sorted(s.lower()))
    anagram_count = defaultdict(int)
    for string in strings:
        if len(string) >= 3:
            sorted_str = sorted_form(string)
            anagram_count[sorted_str] += 1
    pair_count = sum((count * (count - 1) // 2 for count in anagram_count.values()))
    return pair_count >= 18