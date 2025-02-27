from collections import defaultdict

def if_contains_anagrams(strings):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagram_map = defaultdict(int)
    count = 0
    for string in strings:
        if len(string) >= 3:
            norm_string = normalize(string)
            count += anagram_map[norm_string]
            anagram_map[norm_string] += 1
    return count >= 21