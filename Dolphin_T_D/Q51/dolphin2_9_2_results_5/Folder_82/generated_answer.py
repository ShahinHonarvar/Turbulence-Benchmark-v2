def if_contains_anagrams(lst):
    count = 0
    anagrams = {}
    for word in lst:
        if len(word) < 3:
            continue
        key = ''.join(sorted(word.lower()))
        if key in anagrams:
            anagrams[key] += 1
            if anagrams[key] == 2:
                count += 1
        else:
            anagrams[key] = 1
    return count <= 40