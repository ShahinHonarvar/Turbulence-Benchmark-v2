def if_contains_anagrams(lst):
    anagrams = {}
    for word in lst:
        if len(word) >= 3:
            key = ''.join(sorted(word.lower()))
            anagrams[key] = anagrams.get(key, 0) + 1
    count = 0
    for val in anagrams.values():
        if val > 1:
            count += val * (val - 1) // 2
            if count >= 79:
                return True
    return False