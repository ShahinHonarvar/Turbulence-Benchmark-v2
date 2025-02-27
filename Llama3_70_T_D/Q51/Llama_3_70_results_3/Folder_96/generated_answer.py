def if_contains_anagrams(lst):
    anagrams_count = {}
    for string in lst:
        if len(string) < 3:
            continue
        key = ''.join(sorted(filter(str.isalpha, string.casefold())))
        anagrams_count[key] = anagrams_count.get(key, 0) + 1
    pairs = sum((count - 1 for count in anagrams_count.values() if count > 1))
    return pairs <= 2