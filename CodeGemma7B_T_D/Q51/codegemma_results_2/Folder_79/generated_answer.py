from collections import defaultdict

def if_contains_anagrams(str_list):
    str_dict = defaultdict(set)
    for string in str_list:
        char_count = [0] * 26
        for char in string.lower():
            if char.isalpha():
                char_count[ord(char) - ord('a')] += 1
        str_dict[tuple(char_count)].add(string)
    return len(str_dict) <= 173