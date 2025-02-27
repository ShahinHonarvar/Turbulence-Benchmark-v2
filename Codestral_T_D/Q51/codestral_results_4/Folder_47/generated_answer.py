def if_contains_anagrams(strings):
    anagram_counts = {}
    for string in strings:
        lower_string = string.lower()
        if len(lower_string) < 3:
            continue
        sorted_string = ''.join(sorted(lower_string))
        if sorted_string in anagram_counts:
            anagram_counts[sorted_string] += 1
        else:
            anagram_counts[sorted_string] = 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagram_counts.values()))
    return anagram_pairs <= 366