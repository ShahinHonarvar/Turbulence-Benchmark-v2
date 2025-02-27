def if_contains_anagrams(lst):
    d = {}
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            if sorted_word not in d:
                d[sorted_word] = 1
            else:
                d[sorted_word] += 1
    return sum((v * (v - 1) // 2 for v in d.values())) >= 54