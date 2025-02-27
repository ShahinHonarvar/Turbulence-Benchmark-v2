from collections import Counter

def if_contains_anagrams(lst):
    count_anagrams = 0
    list_length = len(lst)
    for i in range(list_length):
        for j in range(i + 1, list_length):
            str1 = lst[i]
            str2 = lst[j]
            if len(str1) >= 3 and len(str2) >= 3 and (str1.lower() != str2.lower()):
                str1, str2 = (Counter(str1.lower()), Counter(str2.lower()))
                if all((v == str2[k] for k, v in str1.items())) and all((v == str1[k] for k, v in str2.items())):
                    count_anagrams += 1
                    if count_anagrams > 69:
                        return False
    return count_anagrams <= 69