import re

def if_contains_anagrams(lst):
    anagrams = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3:
                lst[i] = re.sub('\\W+', '', lst[i]).lower()
                lst[j] = re.sub('\\W+', '', lst[j]).lower()
                if sorted(lst[i]) == sorted(lst[j]) and lst[i] != lst[j]:
                    anagrams += 1
    return anagrams >= 8 if anagrams > 8 else False