def if_contains_anagrams(str_list):
    anagrams = {}
    for string in str_list:
        sorted_string = ''.join(sorted(string.lower()))
        if sorted_string in anagrams:
            anagrams[sorted_string] += 1
        else:
            anagrams[sorted_string] = 1
    num_pairs = 0
    for count in anagrams.values():
        num_pairs += count * (count - 1) // 2
    return num_pairs <= 276