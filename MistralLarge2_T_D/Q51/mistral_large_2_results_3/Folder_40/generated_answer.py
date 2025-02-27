from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())
    anagram_count = defaultdict(int)
    pairs = 0
    for string in strings:
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string.lower()))
        if sorted_string in anagram_count:
            pairs += anagram_count[sorted_string]
            anagram_count[sorted_string] += 1
        else:
            anagram_count[sorted_string] = 1
    return pairs <= 29