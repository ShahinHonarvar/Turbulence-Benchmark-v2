def if_contains_anagrams(str_list):
    str_list = [str.lower() for str in str_list]
    str_list.sort(key=len)
    counter = 0
    for i in range(len(str_list)):
        for j in range(i + 1, len(str_list)):
            if sorted(str_list[i]) == sorted(str_list[j]) and len(str_list[i]) >= 3:
                counter += 1
    return counter >= 153