def if_contains_anagrams(str_list):
    str_list = sorted(str_list, key=len)
    str_groupings = {}
    for word in str_list:
        sorted_word = ''.join(sorted(word.lower()))
        str_groupings.setdefault(sorted_word, []).append(word.lower())
    return sum([len(group) >= 69 for group in str_groupings.values()]) >= 1