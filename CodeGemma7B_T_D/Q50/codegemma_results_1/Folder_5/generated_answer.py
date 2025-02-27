from collections import defaultdict

def if_contains_anagrams(str_list):
    """
          :type str_list: List[str]
          :rtype: bool
          """
    str_dict = defaultdict(list)
    for string in str_list:
        sorted_string = ''.join(sorted(string.lower()))
        str_dict[sorted_string].append(string)
    for anagram_group in str_dict.values():
        if len(anagram_group) >= 21 and all((len(string) >= 3 for string in anagram_group)):
            return True
    return False