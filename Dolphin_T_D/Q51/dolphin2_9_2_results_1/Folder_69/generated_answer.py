from collections import Counter

def if_contains_anagrams(lst_str):
    count = 0
    for i in range(len(lst_str)):
        for j in range(i + 1, len(lst_str)):
            if len(lst_str[i]) >= 3 and len(lst_str[j]) >= 3:
                if Counter(lst_str[i].lower()) == Counter(lst_str[j].lower()):
                    count += 1
                    if count >= 58:
                        return True
    return False