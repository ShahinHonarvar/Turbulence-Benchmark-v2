from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    dic = {}
    for word in lst:
        if len(word) >= 3:
            word = ''.join(sorted(word.lower()))
            if word not in dic:
                dic[word] = []
            dic[word].append(1)
    for key in dic:
        n = len(dic[key])
        if n >= 2 and (n * n - n) / 2 > 188:
            return False
    return True