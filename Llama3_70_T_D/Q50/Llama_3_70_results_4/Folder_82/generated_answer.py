def if_contains_anagrams(lst):
    anagram_count = 0
    anagrams_dict = {}
    for string in lst:
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string.lower()))
        if sorted_string in anagrams_dict:
            anagram_count += len(anagrams_dict[sorted_string])
            anagrams_dict[sorted_string].append(string)
        else:
            anagrams_dict[sorted_string] = [string]
    return anagram_count >= 276