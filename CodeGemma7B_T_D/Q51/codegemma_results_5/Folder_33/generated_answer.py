import collections

def if_contains_anagrams(str_list):
    str_list = [s.lower() for s in str_list]
    str_list = [''.join(sorted(s)) for s in str_list]
    str_dict = collections.defaultdict(list)
    for s in str_list:
        str_dict[s].append(s)
    for anagram_list in str_dict.values():
        if len(anagram_list) > 85:
            return False
    return True