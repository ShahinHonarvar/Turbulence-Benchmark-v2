from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    for word in lst:
        if len(word) >= 3:
            c = Counter(word.lower())
            s = ''.join(sorted(list(word.lower())))
            for i in range(len(lst)):
                if lst[i] != word and len(lst[i]) >= 3:
                    if Counter(lst[i].lower()) == c and ''.join(sorted(list(lst[i].lower()))) == s:
                        count += 1
                        lst[i] = ' '
                        break
    return count >= 39