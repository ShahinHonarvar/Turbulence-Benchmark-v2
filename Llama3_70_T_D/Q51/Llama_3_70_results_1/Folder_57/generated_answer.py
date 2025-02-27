def if_contains_anagrams(lst):
    anagrams_count = {}
    for string in lst:
        lower_string = string.lower()
        sorted_string = ''.join(sorted(lower_string))
        if len(lower_string) >= 3 and lower_string.isalpha():
            if sorted_string in anagrams_count:
                anagrams_count[sorted_string] += 1
            else:
                anagrams_count[sorted_string] = 1
    anagrams_pairs = sum((n * (n - 1) // 2 for n in anagrams_count.values()))
    return anagrams_pairs <= 74