def if_contains_anagrams(str_list):

    def helper(str):
        tmp = sorted(str.lower())
        return ''.join(tmp)
    str_dict = {}
    for word in str_list:
        rstr = helper(word)
        str_dict.setdefault(rstr, []).append(word)
    pairs = 0
    for key, words in str_dict.items():
        if len(words) >= 3:
            pairs += len(words) - 2
    return pairs <= 84