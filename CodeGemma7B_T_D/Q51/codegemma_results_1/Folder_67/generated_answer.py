import re

def if_contains_anagrams(str_list):
    for i in range(len(str_list)):
        for j in range(i + 1, len(str_list)):
            a = re.sub('[^a-zA-Z]', '', str_list[i]).lower()
            b = re.sub('[^a-zA-Z]', '', str_list[j]).lower()
            if len(a) >= 3 and len(b) >= 3 and (sorted(a) == sorted(b)):
                return False
    return True