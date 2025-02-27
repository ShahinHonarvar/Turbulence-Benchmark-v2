def if_contains_anagrams(strings):
    anagrams_count = {}
    for string in strings:
        string = ''.join(filter(str.isalpha, string)).lower()
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string))
        if sorted_string in anagrams_count:
            anagrams_count[sorted_string] += 1
        else:
            anagrams_count[sorted_string] = 1
    return sum((count - 1 for count in anagrams_count.values() if count > 1)) <= 36