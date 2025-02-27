from collections import Counter

def if_contains_anagrams(str_list):
    str_list = [s.lower() for s in str_list]
    str_list = [s for s in str_list if len(s) >= 3]
    count = 0
    for i in range(len(str_list)):
        for j in range(i + 1, len(str_list)):
            if Counter(str_list[i]) == Counter(str_list[j]):
                count += 1
                if count >= 42:
                    return True
    return False