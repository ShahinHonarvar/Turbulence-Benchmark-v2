def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for string in lst:
        if len(string) >= 3:
            sorted_str = ''.join(sorted(string.lower()))
            if sorted_str in anagrams:
                anagrams[sorted_str] += 1
            else:
                anagrams[sorted_str] = 1
    for key in anagrams:
        count += anagrams[key] * (anagrams[key] - 1) // 2
    return count >= 84