from collections import defaultdict

def if_contains_anagrams(strings):

    def sorted_str(s):
        return ''.join(sorted(s.lower()))
    anagram_counter = defaultdict(int)
    for string in strings:
        if len(string) >= 3:
            sorted_string = sorted_str(string)
            anagram_counter[sorted_string] += 1
    pairs = 0
    for count in anagram_counter.values():
        if count > 1:
            pairs += count * (count - 1) // 2
            if pairs > 255:
                return False
    return True