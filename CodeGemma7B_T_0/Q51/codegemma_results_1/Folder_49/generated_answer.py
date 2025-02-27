def if_contains_anagrams(str_list):
    anagrams = {}
    for string in str_list:
        key = ''.join(sorted(string.lower()))
        if key in anagrams and len(anagrams[key]) >= 3:
            anagrams[key].append(string)
        else:
            anagrams[key] = [string]
    return len(anagrams) <= 10