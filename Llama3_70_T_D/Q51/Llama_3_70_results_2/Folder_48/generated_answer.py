def if_contains_anagrams(strings):
    counter = {}
    anagram_count = 0
    for string in strings:
        string_lower = ''.join(filter(str.isalpha, string)).lower()
        if len(string_lower) < 3:
            continue
        sorted_string = ''.join(sorted(string_lower))
        if sorted_string in counter:
            counter[sorted_string] += 1
        else:
            counter[sorted_string] = 1
    for count in counter.values():
        anagram_count += count * (count - 1) // 2
    return anagram_count <= 277