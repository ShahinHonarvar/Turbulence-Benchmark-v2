def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for i in lst:
        i = i.lower()
        if len(i) < 3:
            continue
        sorted_str = ''.join(sorted(i))
        if sorted_str in anagrams:
            anagrams[sorted_str].append(i)
        else:
            anagrams[sorted_str] = [i]
    for k in anagrams.keys():
        count += len(anagrams[k]) * (len(anagrams[k]) - 1) // 2
        if count >= 314:
            return True
    return False