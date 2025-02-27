def if_contains_anagrams(str_list):
    str_list = [word.lower().replace(' ', '') for word in str_list]
    str_list.sort(key=len)
    str_dict = {}
    count = 0
    for word in str_list:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word))
        if sorted_word in str_dict:
            count += 1
            if count >= 89:
                return True
        else:
            str_dict[sorted_word] = word
    return False