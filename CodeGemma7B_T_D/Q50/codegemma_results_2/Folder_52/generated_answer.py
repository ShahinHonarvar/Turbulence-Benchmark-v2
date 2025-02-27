def if_contains_anagrams(str_list):
    str_dict = {}
    for word in str_list:
        key = ''.join(sorted(word.lower()))
        if key in str_dict:
            str_dict[key].append(word)
        else:
            str_dict[key] = [word]
    count = 0
    for anagrams in str_dict.values():
        if len(anagrams) >= 3:
            count += len(anagrams) * (len(anagrams) - 1) // 2
    return count >= 58