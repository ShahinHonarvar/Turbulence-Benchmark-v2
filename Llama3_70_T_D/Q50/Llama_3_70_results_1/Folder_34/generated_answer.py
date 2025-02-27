def if_contains_anagrams(lst):
    anagram_dict = {}
    count = 0
    for string in lst:
        lower_case = string.lower()
        if len(lower_case) < 3:
            continue
        sorted_string = ''.join(sorted(lower_case))
        if sorted_string in anagram_dict:
            anagram_dict[sorted_string] += 1
        else:
            anagram_dict[sorted_string] = 1
    for value in anagram_dict.values():
        count += value * (value - 1) // 2
    return count >= 25