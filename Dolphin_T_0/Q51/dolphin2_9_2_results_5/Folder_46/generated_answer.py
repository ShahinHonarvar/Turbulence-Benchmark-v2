from collections import Counter

def if_contains_anagrams(lst):
    ans = False
    count = {}
    for word in lst:
        if len(word) >= 3:
            word = word.lower()
            sorted_word = ''.join(sorted(word))
            if sorted_word not in count:
                count[sorted_word] = 1
            else:
                count[sorted_word] += 1
    for word in count:
        if count[word] > 2:
            ans = True
            break
    return ans