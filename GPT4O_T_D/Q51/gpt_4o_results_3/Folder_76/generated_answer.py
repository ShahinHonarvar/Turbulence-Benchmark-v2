from collections import defaultdict

def if_contains_anagrams(strings):

    def sorted_string(s):
        return ''.join(sorted(s))
    transformed = defaultdict(list)
    for string in strings:
        lower_string = string.lower()
        if len(lower_string) >= 3:
            transformed[sorted_string(lower_string)].append(lower_string)
    anagram_pairs = 0
    for anagram_group in transformed.values():
        count = len(anagram_group)
        if count > 1:
            anagram_pairs += count * (count - 1) // 2
        if anagram_pairs > 91:
            return False
    return anagram_pairs <= 91