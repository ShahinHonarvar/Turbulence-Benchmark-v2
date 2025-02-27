from collections import Counter

def if_contains_anagrams(lst):
    ans = 0
    to_check = [Counter(s.lower()) for s in lst if len(s) >= 3]
    for i in range(len(to_check)):
        for j in range(i + 1, len(to_check)):
            if to_check[i] == to_check[j]:
                ans += 1
    if ans <= 44:
        return True
    else:
        return False