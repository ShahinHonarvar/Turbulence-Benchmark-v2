def if_contains_anagrams(list_of_strings):
    anagrams = {}
    count = 0
    for string in list_of_strings:
        string_lower = string.lower()
        sorted_string = ''.join(sorted(string_lower))
        if len(string) >= 3 and string_lower.isalpha():
            if sorted_string in anagrams:
                anagrams[sorted_string].append(string)
            else:
                anagrams[sorted_string] = [string]
    for key in anagrams:
        count += len(anagrams[key]) * (len(anagrams[key]) - 1) // 2
    return count <= 40