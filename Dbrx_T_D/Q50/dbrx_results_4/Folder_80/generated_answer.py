def if_contains_anagrams(strings):
    anagrams_dict = {}
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            if sorted_string in anagrams_dict:
                anagrams_dict[sorted_string] += 1
            else:
                anagrams_dict[sorted_string] = 1
    total_anagrams = sum(map(lambda x: x // 2, anagrams_dict.values()))
    return total_anagrams >= 19