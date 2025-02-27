def if_contains_anagrams(lst):
    count = {}
    total_anagrams = 0
    for s in lst:
        s = ''.join(filter(str.isalpha, s)).lower()
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s))
        if sorted_s in count:
            count[sorted_s].append(s)
        else:
            count[sorted_s] = [s]
    for value in count.values():
        total_anagrams += len(value) * (len(value) - 1) // 2
    return total_anagrams <= 206