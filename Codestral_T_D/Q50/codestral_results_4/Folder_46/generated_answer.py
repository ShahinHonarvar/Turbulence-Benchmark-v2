def if_contains_anagrams(lst):
    d = {}
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            if sorted_word in d:
                d[sorted_word] += 1
            else:
                d[sorted_word] = 1
    count = 0
    for k, v in d.items():
        count += v * (v - 1) // 2
    return count >= 38