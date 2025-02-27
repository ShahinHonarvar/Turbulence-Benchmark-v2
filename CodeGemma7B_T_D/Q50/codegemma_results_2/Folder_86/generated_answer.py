from collections import defaultdict

def if_contains_anagrams(str_list):
    dict1 = defaultdict(int)
    for s in str_list:
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                str2 = sorted(s[i:j + 1].lower())
                str1 = ''.join(str2)
                dict1[str1] += 1
    count = 0
    for v in dict1.values():
        if v >= 2:
            count += 1
    return count >= 115