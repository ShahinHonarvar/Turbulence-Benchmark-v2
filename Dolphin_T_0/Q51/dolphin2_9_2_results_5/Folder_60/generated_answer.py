from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    anagrams_count = {}
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            str1 = ''.join(sorted(lst[i].lower()))
            str2 = ''.join(sorted(lst[j].lower()))
            if len(str1) < 3 or len(str2) < 3:
                continue
            if str1 == str2:
                pair = (lst[i], lst[j])
                anagrams_count[pair] = anagrams_count.get(pair, 0) + 1
                if anagrams_count[pair] == 2:
                    count += 1
                if count >= 77:
                    return True
    return count >= 77