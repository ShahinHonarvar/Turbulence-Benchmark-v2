import collections

def if_contains_anagrams(str_list):
    str_dict = collections.defaultdict(list)
    for word in str_list:
        sorted_word = ''.join(sorted([c for c in word.lower() if c.isalpha() and len(c) >= 3]))
        str_dict[sorted_word].append(word)
    return len(str_dict) <= 46