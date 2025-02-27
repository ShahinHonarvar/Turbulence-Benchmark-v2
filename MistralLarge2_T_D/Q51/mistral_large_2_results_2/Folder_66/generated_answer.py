from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(list)
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        anagram_dict[sorted_string].append(string)
    count = 0
    for key, value in anagram_dict.items():
        if len(key) >= 3 and len(value) > 1:
            count += len(value) * (len(value) - 1) // 2
    return count <= 64