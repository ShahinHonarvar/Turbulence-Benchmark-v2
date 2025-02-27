def if_contains_anagrams(lst):
    anagrams_count = {}
    for string in lst:
        string = ''.join(filter(str.isalpha, string)).lower()
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string))
        if sorted_string in anagrams_count:
            anagrams_count[sorted_string] += 1
        else:
            anagrams_count[sorted_string] = 1
    pairs_count = sum(((count - 1) * count // 2 for count in anagrams_count.values() if count > 1))
    return pairs_count <= 67