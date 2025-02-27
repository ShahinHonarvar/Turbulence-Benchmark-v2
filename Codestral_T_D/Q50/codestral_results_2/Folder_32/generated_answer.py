def if_contains_anagrams(lst):
    d = {}
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        if len(word) >= 3:
            if sorted_word in d:
                d[sorted_word] += 1
            else:
                d[sorted_word] = 1
    count = 0
    for value in d.values():
        count += value * (value - 1) // 2
    return count >= 194