def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for string in lst:
        sorted_string = ''.join(sorted(string.lower()))
        if len(string) >= 3:
            if sorted_string in anagrams:
                anagrams[sorted_string] += 1
            else:
                anagrams[sorted_string] = 1
    for key in anagrams:
        if anagrams[key] > 1:
            count += anagrams[key] * (anagrams[key] - 1) // 2
    return count >= 70