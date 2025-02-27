from collections import defaultdict

def if_contains_anagrams(strings):

    def sort_string(s):
        return ''.join(sorted(s.lower()))
    each_length_count = defaultdict(int)
    for string in strings:
        if len(string) >= 3:
            sorted_str = sort_string(string)
            each_length_count[sorted_str] += 1
    anagram_pairs = 0
    for count in each_length_count.values():
        if count > 1:
            anagram_pairs += count * (count - 1) // 2
            if anagram_pairs > 61:
                return False
    return anagram_pairs <= 61