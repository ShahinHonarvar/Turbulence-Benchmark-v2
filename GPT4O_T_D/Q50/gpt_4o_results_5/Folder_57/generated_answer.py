from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(int)
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            anagram_dict[sorted_string] += 1
    anagram_count = 0
    for count in anagram_dict.values():
        if count > 1:
            anagram_count += count * (count - 1) // 2
            if anagram_count >= 50:
                return True
    return False