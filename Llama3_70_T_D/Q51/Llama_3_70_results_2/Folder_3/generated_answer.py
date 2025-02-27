def if_contains_anagrams(lst):
    anagram_count = {}
    for string in lst:
        temp_string = ''.join(filter(str.isalpha, string)).lower()
        if len(temp_string) < 3:
            continue
        sorted_string = ''.join(sorted(temp_string))
        if sorted_string in anagram_count:
            anagram_count[sorted_string] += 1
        else:
            anagram_count[sorted_string] = 1
    pairs = 0
    for count in anagram_count.values():
        pairs += count * (count - 1) // 2
    return pairs <= 66