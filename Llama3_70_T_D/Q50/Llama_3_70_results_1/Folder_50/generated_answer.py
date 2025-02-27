def if_contains_anagrams(lst):
    anagrams = {}
    for string in lst:
        lower_string = string.lower()
        sorted_string = ''.join(sorted(lower_string))
        if len(lower_string) >= 3:
            if sorted_string in anagrams:
                anagrams[sorted_string] += 1
            else:
                anagrams[sorted_string] = 1
    count = 0
    for value in anagrams.values():
        count += value * (value - 1) // 2
    return count >= 20