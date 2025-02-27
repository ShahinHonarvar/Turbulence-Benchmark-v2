def if_contains_anagrams(strings):
    anagram_count = 0
    anagram_dict = {}
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) < 3:
            continue
        if sorted_string in anagram_dict:
            anagram_count += len(anagram_dict[sorted_string])
            anagram_dict[sorted_string].append(string)
            if anagram_count >= 59:
                return True
        else:
            anagram_dict[sorted_string] = [string]
    return False