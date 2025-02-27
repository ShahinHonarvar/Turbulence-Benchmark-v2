def if_contains_anagrams(str_list):
    seen = set()
    anagram_count = 0
    for string in str_list:
        string = ''.join(sorted(string.lower()))
        if len(string) >= 3 and string not in seen:
            seen.add(string)
            for other_string in str_list:
                if string != other_string:
                    other_string = ''.join(sorted(other_string.lower()))
                    if string == other_string:
                        anagram_count += 1
        if anagram_count >= 30:
            return True
    return False