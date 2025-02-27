def if_contains_anagrams(lst):
    count = 0
    anagrams_dict = {}
    for string in lst:
        string_lower = string.lower()
        if len(string_lower) >= 3:
            sorted_chars = ''.join(sorted(string_lower))
            if sorted_chars in anagrams_dict:
                anagrams_dict[sorted_chars].append(string_lower)
            else:
                anagrams_dict[sorted_chars] = [string_lower]
    for key in anagrams_dict:
        if len(anagrams_dict[key]) > 1:
            count += len(anagrams_dict[key]) * (len(anagrams_dict[key]) - 1) // 2
    return count >= 19