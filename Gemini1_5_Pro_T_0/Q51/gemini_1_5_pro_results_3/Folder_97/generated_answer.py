from collections import defaultdict

def if_contains_anagrams(list_of_strings):
    anagram_dict = defaultdict(lambda: [])
    for string in list_of_strings:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            anagram_dict[sorted_string].append(string)
    count = 0
    for key in anagram_dict:
        n = len(anagram_dict[key])
        if n >= 2:
            count += n * (n - 1) // 2
    return count <= 18