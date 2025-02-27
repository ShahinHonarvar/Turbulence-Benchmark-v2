def if_contains_anagrams(str_list):
    str_set = set()
    pairs = 0
    for string in str_list:
        string = string.lower()
        string = ''.join(sorted(string))
        if string in str_set:
            pairs += 1
        else:
            str_set.add(string)
    if pairs >= 74:
        return True
    else:
        return False