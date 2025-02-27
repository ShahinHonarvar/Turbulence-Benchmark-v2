def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for string in lst:
        sorted_str = ''.join(sorted(string.lower()))
        if len(string) >= 3:
            if sorted_str in anagrams:
                anagrams[sorted_str].append(string)
            else:
                anagrams[sorted_str] = [string]
    for key in anagrams:
        count += len(anagrams[key]) * (len(anagrams[key]) - 1) // 2
    return count >= 177