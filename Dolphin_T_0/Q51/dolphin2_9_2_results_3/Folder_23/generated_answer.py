from collections import Counter

def if_contains_anagrams(lst):
    ans = 0
    dic = {}
    for i in range(len(lst)):
        word = lst[i]
        if len(word) < 3:
            continue
        word = word.lower()
        c = Counter(word)
        c = str(c)
        if c in dic:
            dic[c] += 1
            ans += dic[c]
            if dic[c] == 2:
                dic[c] = 0
                ans -= 1
        else:
            dic[c] = 0
    return ans <= 98