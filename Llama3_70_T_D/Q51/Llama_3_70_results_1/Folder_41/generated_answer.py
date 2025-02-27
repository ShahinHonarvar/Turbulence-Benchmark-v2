def if_contains_anagrams(lst):
    anagrams_count = {}
    for string in lst:
        string_lower = string.lower()
        sorted_string = ''.join(sorted(string_lower))
        if len(string_lower) < 3 or not sorted_string.isalpha():
            continue
        if sorted_string in anagrams_count:
            anagrams_count[sorted_string] += 1
        else:
            anagrams_count[sorted_string] = 1
    pairs = sum((count * (count - 1) // 2 for count in anagrams_count.values()))
    return pairs <= 52