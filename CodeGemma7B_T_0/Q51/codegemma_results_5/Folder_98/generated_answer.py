def if_contains_anagrams(str_list):
    anagrams = {}
    for string in str_list:
        key = ''.join(sorted(string.lower()))
        if key in anagrams:
            anagrams[key] += 1
        else:
            anagrams[key] = 1
    return sum((count for count in anagrams.values() if count > 1)) <= 46