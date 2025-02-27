def if_contains_anagrams(strings):
    count = 0
    normalized_strings = [''.join(sorted(s.lower())) for s in strings if len(s) >= 3]
    string_counter = {}
    for ns in normalized_strings:
        if ns in string_counter:
            count += string_counter[ns]
            if count > 401:
                return False
            string_counter[ns] += 1
        else:
            string_counter[ns] = 1
    return True