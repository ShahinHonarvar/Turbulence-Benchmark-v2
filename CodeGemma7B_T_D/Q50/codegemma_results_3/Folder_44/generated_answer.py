def if_contains_anagrams(str_list):
    anagrams = {}
    for string in str_list:
        temp_dict = {}
        for char in sorted(string.lower()):
            temp_dict[char] = temp_dict.get(char, 0) + 1
        anagrams[tuple(sorted(temp_dict.items()))] = anagrams.get(tuple(sorted(temp_dict.items())), 0) + 1
    count = 0
    for num in anagrams.values():
        count += num * (num - 1) // 2
    return count >= 44