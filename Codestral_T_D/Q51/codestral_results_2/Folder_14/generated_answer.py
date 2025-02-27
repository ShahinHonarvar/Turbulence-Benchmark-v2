def if_contains_anagrams(lst):
    anagrams = {}
    for word in lst:
        key = ''.join(sorted(word.lower()))
        if len(key) >= 3:
            if key in anagrams:
                anagrams[key] += 1
            else:
                anagrams[key] = 1
    count = 0
    for key in anagrams:
        count += anagrams[key] * (anagrams[key] - 1) // 2
    return count <= 474