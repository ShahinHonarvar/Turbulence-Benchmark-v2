from collections import Counter

def if_contains_anagrams(lst):
    ctr = Counter()
    cnt = 0
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            if sorted_word in ctr:
                ctr[sorted_word] += 1
                cnt += 1
            else:
                ctr[sorted_word] = 1
    if cnt >= 16:
        return True
    else:
        return False