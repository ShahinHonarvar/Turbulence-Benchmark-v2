def if_contains_anagrams(lst):
    anagrams_count = {}
    for string in lst:
        lower_string = ''.join(filter(str.isalpha, string.lower()))
        if len(lower_string) < 3:
            continue
        sorted_string = ''.join(sorted(lower_string))
        if sorted_string in anagrams_count:
            anagrams_count[sorted_string] += 1
        else:
            anagrams_count[sorted_string] = 1
    anagrams_pairs = sum((count * (count - 1) // 2 for count in anagrams_count.values()))
    return anagrams_pairs <= 464