def if_contains_anagrams(lst):
    anagram_counts = {}
    for string in lst:
        string = ''.join(filter(str.isalpha, string)).lower()
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string))
        anagram_counts[sorted_string] = anagram_counts.get(sorted_string, 0) + 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagram_counts.values()))
    return anagram_pairs <= 366