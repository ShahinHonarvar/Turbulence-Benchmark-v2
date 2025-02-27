from collections import defaultdict

def if_contains_anagrams(strings):

    def sort_characters(s):
        return ''.join(sorted(s.lower()))

    def is_valid_anagram(s):
        return len(s) >= 3
    anagram_groups = defaultdict(int)
    for string in strings:
        if is_valid_anagram(string):
            sorted_string = sort_characters(string)
            anagram_groups[sorted_string] += 1
    pair_count = 0
    for count in anagram_groups.values():
        if count > 1:
            pair_count += count * (count - 1) // 2
            if pair_count >= 97:
                return True
    return False