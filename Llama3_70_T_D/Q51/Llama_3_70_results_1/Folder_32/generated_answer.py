def if_contains_anagrams(lst):
    anagrams_count = {}
    for string in lst:
        if len(string) < 3:
            continue
        string = ''.join(filter(str.isalpha, string)).lower()
        sorted_string = ''.join(sorted(string))
        if sorted_string in anagrams_count:
            anagrams_count[sorted_string] += 1
        else:
            anagrams_count[sorted_string] = 1
    pairs_count = sum((count * (count - 1) // 2 for count in anagrams_count.values()))
    return pairs_count <= 89