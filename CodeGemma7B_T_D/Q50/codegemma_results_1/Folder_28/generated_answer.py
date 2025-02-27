def if_contains_anagrams(str_list):
    anagram_counts = {}
    for string in str_list:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            anagram_counts[sorted_string] = anagram_counts.get(sorted_string, 0) + 1
    for count in anagram_counts.values():
        if count >= 81:
            return True
    return False