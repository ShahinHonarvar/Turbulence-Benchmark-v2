def if_contains_anagrams(lst):
    anagram_count = {}
    for string in lst:
        lower_string = ''.join(filter(str.isalpha, string.lower()))
        if len(lower_string) < 3:
            continue
        sorted_string = ''.join(sorted(lower_string))
        if sorted_string in anagram_count:
            anagram_count[sorted_string] += 1
        else:
            anagram_count[sorted_string] = 1
    pairs = sum((value * (value - 1) // 2 for value in anagram_count.values()))
    return pairs <= 38