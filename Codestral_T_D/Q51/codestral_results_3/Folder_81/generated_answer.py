def if_contains_anagrams(strings):
    anagram_counter = {}
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            anagram_counter[sorted_string] = anagram_counter.get(sorted_string, 0) + 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagram_counter.values()))
    return anagram_pairs <= 79