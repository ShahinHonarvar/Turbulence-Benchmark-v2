def if_contains_anagrams(lst_str):
    count = 0
    for i in range(len(lst_str)):
        for j in range(i + 1, len(lst_str)):
            if len(lst_str[i]) >= 3 and len(lst_str[j]) >= 3 and (sorted(lst_str[i].lower()) == sorted(lst_str[j].lower())):
                count += 1
                if count >= 123:
                    return True
    return False