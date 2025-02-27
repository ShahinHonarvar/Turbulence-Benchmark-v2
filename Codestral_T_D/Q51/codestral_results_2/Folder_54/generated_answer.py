def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        lowered_string = string.lower()
        if len(lowered_string) >= 3:
            sorted_string = ''.join(sorted(lowered_string))
            if sorted_string in anagrams:
                anagrams[sorted_string].append(lowered_string)
            else:
                anagrams[sorted_string] = [lowered_string]
    anagram_pairs = sum((len(lst) * (len(lst) - 1) // 2 for lst in anagrams.values()))
    return anagram_pairs <= 39