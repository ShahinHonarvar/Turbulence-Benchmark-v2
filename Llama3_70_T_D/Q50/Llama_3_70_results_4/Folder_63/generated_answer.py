def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for string in lst:
        lower_string = string.lower()
        sorted_string = ''.join(sorted(lower_string))
        if len(lower_string) >= 3:
            if sorted_string in anagrams:
                anagrams[sorted_string].append(lower_string)
            else:
                anagrams[sorted_string] = [lower_string]
    for strings in anagrams.values():
        count += len(strings) * (len(strings) - 1) // 2
    return count >= 89