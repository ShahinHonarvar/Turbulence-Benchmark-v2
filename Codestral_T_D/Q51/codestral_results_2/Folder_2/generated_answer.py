def if_contains_anagrams(strings):
    anagram_groups = {}
    for string in strings:
        lower_string = string.lower()
        if len(lower_string) < 3:
            continue
        sorted_string = ''.join(sorted(lower_string))
        if sorted_string in anagram_groups:
            anagram_groups[sorted_string].append(lower_string)
        else:
            anagram_groups[sorted_string] = [lower_string]
    anagram_pairs = sum((len(group) * (len(group) - 1) // 2 for group in anagram_groups.values()))
    return anagram_pairs <= 81