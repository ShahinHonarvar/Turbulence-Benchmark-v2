from collections import defaultdict

def if_contains_anagrams(strings):

    def sorted_str(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = defaultdict(int)
    count = 0
    for string in strings:
        if len(string) >= 3:
            sorted_string = sorted_str(string)
            count += anagram_dict[sorted_string]
            anagram_dict[sorted_string] += 1
    return count >= 20