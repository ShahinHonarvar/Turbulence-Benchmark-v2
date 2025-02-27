from collections import Counter

def if_contains_anagrams(lst):
    ans = 0
    count = [0] * 1000000
    for string in lst:
        if len(string) < 3:
            continue
        counter = Counter(string.lower())
        num = 0
        for key in counter.keys():
            num = num * 26 + ord(key) - 96
        count[num] += 1
    for i in range(len(count)):
        if count[i] > 1:
            ans += count[i] * (count[i] - 1) // 2
        if ans > 210:
            return False
    return ans <= 210