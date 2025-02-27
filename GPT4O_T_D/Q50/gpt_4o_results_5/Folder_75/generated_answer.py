from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(int)
    for string in strings:
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string.lower()))
        anagram_dict[sorted_string] += 1
    count = 0
    for anagram_count in anagram_dict.values():
        if anagram_count > 1:
            count += anagram_count * (anagram_count - 1) // 2
        if count >= 70:
            return True
    return False