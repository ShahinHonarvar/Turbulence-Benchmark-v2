from collections import defaultdict

def if_contains_anagrams(str_list):
    anagram_dict = defaultdict(int)
    for string in str_list:
        char_count = [0] * 26
        for char in string.lower():
            if char.isalpha() and len(char) >= 3:
                char_count[ord(char) - ord('a')] += 1
        sorted_count = sorted(char_count)
        tuple_count = tuple(sorted_count)
        anagram_dict[tuple_count] += 1
        if anagram_dict[tuple_count] > 210:
            return False
    return True