def if_contains_anagrams(strings):
    anagrams_count = {}
    for string in strings:
        lower_string = string.lower()
        filtered_string = ''.join(filter(str.isalpha, lower_string))
        if len(filtered_string) < 3:
            continue
        sorted_string = ''.join(sorted(filtered_string))
        if sorted_string in anagrams_count:
            anagrams_count[sorted_string] += 1
        else:
            anagrams_count[sorted_string] = 1
    pairs_count = sum((count * (count - 1) // 2 for count in anagrams_count.values()))
    return pairs_count <= 276