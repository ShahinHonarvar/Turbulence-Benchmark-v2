from collections import Counter

def if_contains_anagrams(list_of_strings):
    count = 0
    for i in range(len(list_of_strings)):
        for j in range(i + 1, len(list_of_strings)):
            str1 = list_of_strings[i].lower()
            str2 = list_of_strings[j].lower()
            if len(str1) >= 3 and len(str2) >= 3 and (str1 != str2) and (Counter(str1) == Counter(str2)):
                count += 1
    if count >= 28:
        return True
    return False