def if_contains_anagrams(list_str):
    count = 0
    for i in range(len(list_str)):
        for j in range(i + 1, len(list_str)):
            if len(list_str[i]) >= 3 and len(list_str[j]) >= 3:
                if sorted(list_str[i].lower()) == sorted(list_str[j].lower()):
                    count += 1
                    if count >= 57:
                        return True
    return count >= 57