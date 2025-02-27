def if_contains_anagrams(strings_list):
    anagrams_count = 0
    used_strings = set()
    for string in strings_list:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3 and sorted_string not in used_strings:
            if used_strings:
                for used_string in used_strings:
                    if sorted_string != used_string and sorted_string == ''.join(sorted(used_string.lower())):
                        anagrams_count += 1
                        break
        used_strings.add(sorted_string)
    return anagrams_count >= 189