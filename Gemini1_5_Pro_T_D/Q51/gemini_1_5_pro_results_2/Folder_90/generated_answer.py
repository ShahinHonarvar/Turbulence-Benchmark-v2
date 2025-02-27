from collections import defaultdict

def if_contains_anagrams(list_of_strings):
    anagram_dict = defaultdict(lambda: [])
    for str_in in list_of_strings:
        if len(str_in) >= 3:
            sorted_string = ''.join(sorted(str_in.lower()))
            anagram_dict[sorted_string].append(str_in)
    count = 0
    for key in anagram_dict:
        n = len(anagram_dict[key])
        if n >= 2:
            count += n * (n - 1) / 2
    if count <= 147:
        return True
    else:
        return False