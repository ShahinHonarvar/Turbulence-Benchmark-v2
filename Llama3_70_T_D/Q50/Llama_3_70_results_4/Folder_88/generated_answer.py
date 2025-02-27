def if_contains_anagrams(str_list):
    anagrams = {}
    count = 0
    for string in str_list:
        lower_string = string.lower()
        if len(lower_string) >= 3:
            sorted_string = ''.join(sorted(lower_string))
            if sorted_string in anagrams:
                anagrams[sorted_string].append(lower_string)
            else:
                anagrams[sorted_string] = [lower_string]
    for key in anagrams:
        count += len(anagrams[key]) * (len(anagrams[key]) - 1) // 2
    return count >= 34