def if_contains_anagrams(list_of_strings):
    anagram_counts = {}
    for string in list_of_strings:
        string = string.lower()
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string))
        if sorted_string not in anagram_counts:
            anagram_counts[sorted_string] = 1
        else:
            anagram_counts[sorted_string] += 1
    count = 0
    for entry in anagram_counts.values():
        count += entry * (entry - 1) // 2
    return count <= 279