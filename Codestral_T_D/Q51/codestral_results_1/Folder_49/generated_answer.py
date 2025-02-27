def if_contains_anagrams(strings):
    anagram_count = 0
    anagram_dict = {}
    for string in strings:
        lower_string = string.lower()
        sorted_string = ''.join(sorted(lower_string))
        if len(lower_string) < 3:
            continue
        if sorted_string not in anagram_dict:
            anagram_dict[sorted_string] = [lower_string]
        else:
            anagram_dict[sorted_string].append(lower_string)
        if len(anagram_dict[sorted_string]) >= 2:
            anagram_count += 1
        if anagram_count > 10:
            return False
    return True