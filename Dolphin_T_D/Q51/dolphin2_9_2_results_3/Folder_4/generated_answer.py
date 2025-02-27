from collections import Counter

def if_contains_anagrams(lst):
    ans = 0
    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            str1 = lst[i].lower()
            str2 = lst[j].lower()
            if len(str1) >= 3 and len(str2) >= 3 and (Counter(str1) == Counter(str2)):
                ans += 1
    return ans <= 84