def if_contains_anagrams(str_list):
    str_list.sort(key=len)
    pairs = 0
    for i in range(len(str_list)):
        for j in range(i + 1, len(str_list)):
            if sorted(str_list[i].lower()) == sorted(str_list[j].lower()) and len(str_list[i]) >= 3:
                pairs += 1
                if pairs > 188:
                    return False
    return True