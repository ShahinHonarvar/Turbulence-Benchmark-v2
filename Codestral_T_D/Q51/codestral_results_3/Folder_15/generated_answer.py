def if_contains_anagrams(strings):
    anagram_count = {}
    pair_count = 0
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            anagram_count[sorted_string] = anagram_count.get(sorted_string, 0) + 1
            if anagram_count[sorted_string] > 1:
                pair_count += 1
    return pair_count <= 20