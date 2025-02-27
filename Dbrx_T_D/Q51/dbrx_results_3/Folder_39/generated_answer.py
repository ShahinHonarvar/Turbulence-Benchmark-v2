def if_contains_anagrams(strings):
    anagram_count = 0
    for string in strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            if strings.count(sorted_string) > 1:
                anagram_count += strings.count(sorted_string)
                if anagram_count > 257:
                    return False
    return True