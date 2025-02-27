from collections import defaultdict

def if_contains_anagrams(str_list):
    str_dict = defaultdict(int)
    for word in str_list:
        word = ''.join(sorted([c for c in word.lower() if c.isalpha() and len(c) >= 3]))
        str_dict[word] += 1
    return len(str_dict) <= 474