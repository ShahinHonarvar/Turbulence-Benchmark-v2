def if_contains_anagrams(strings):
    string_length = {}
    for string in strings:
        string_lowercase = string.lower()
        sorted_string = ''.join(sorted(string_lowercase))
        if len(string_lowercase) >= 3:
            if sorted_string in string_length:
                string_length[sorted_string] += 1
            else:
                string_length[sorted_string] = 1
    count = 0
    for key in string_length:
        if string_length[key] >= 2:
            count += 1
    if count >= 38:
        return True
    else:
        return False