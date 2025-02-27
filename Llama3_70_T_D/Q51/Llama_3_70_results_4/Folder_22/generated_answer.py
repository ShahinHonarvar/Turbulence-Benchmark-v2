def if_contains_anagrams(lst):
    anagrams_count = {}
    for string in lst:
        string = ''.join(filter(str.isalpha, string)).lower()
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string))
        anagrams_count[sorted_string] = anagrams_count.get(sorted_string, 0) + 1
    pairs_count = sum((count * (count - 1) // 2 for count in anagrams_count.values()))
    return pairs_count <= 14