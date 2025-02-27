from collections import Counter

def if_contains_anagrams(lst_of_strings):
    count = 0
    for i in range(len(lst_of_strings)):
        for j in range(i + 1, len(lst_of_strings)):
            str1 = sorted(lst_of_strings[i].lower())
            str2 = sorted(lst_of_strings[j].lower())
            if len(str1) >= 3 and len(str2) >= 3 and (Counter(str1) == Counter(str2)):
                count += 1
                if count >= 19:
                    return True
    if count < 19:
        return False