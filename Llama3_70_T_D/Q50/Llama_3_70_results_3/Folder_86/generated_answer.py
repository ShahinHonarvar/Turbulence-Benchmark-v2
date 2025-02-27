def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for item in lst:
        if len(item) < 3:
            continue
        sorted_item = ''.join(sorted(item.lower()))
        if sorted_item in anagrams:
            anagrams[sorted_item].append(item)
        else:
            anagrams[sorted_item] = [item]
    for key in anagrams:
        count += len(anagrams[key]) * (len(anagrams[key]) - 1) // 2
    return count >= 115