def if_contains_anagrams(strings):
    anagrams = 0
    for string in strings:
        if len(string) >= 3:
            for compare_string in strings:
                if string.lower() != compare_string.lower() and sorted(string.lower()) == sorted(compare_string.lower()):
                    anagrams += 1
    return anagrams >= 44