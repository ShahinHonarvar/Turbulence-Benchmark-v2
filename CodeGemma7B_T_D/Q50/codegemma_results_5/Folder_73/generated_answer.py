from collections import defaultdict

def if_contains_anagrams(str_list):
    """
    Returns true if there are at least 91 pairs of anagrams in the given list; otherwise, it returns false. The function should only consider the anagrams of the length of at least three. The function should compare the strings in a case-insensitive manner.
    """
    str_dict = defaultdict(list)
    for str in str_list:
        str = str.lower()
        str = ''.join(sorted(str))
        str_dict[str].append(str)
    return len([val for val in str_dict.values() if len(val) >= 3 and len(val) >= 91]) >= 1