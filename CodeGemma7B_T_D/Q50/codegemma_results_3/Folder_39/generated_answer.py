def if_contains_anagrams(str_list):
    str_list = [x.lower() + x.count(letter) for x in str_list for letter in string.ascii_lowercase if x.count(letter) > 2]
    str_list.sort()
    for i in range(len(str_list)):
        for j in range(i + 1, len(str_list)):
            if str_list[i] == str_list[j]:
                return True
    return False