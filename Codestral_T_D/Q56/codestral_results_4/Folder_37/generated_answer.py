def all_substring_of_size_n(input_string):
    if len(input_string) < 65:
        return []
    else:
        substrings = set()
        for i in range(len(input_string) - 64):
            substring = input_string[i:i + 65]
            if len(set(substring)) == 65:
                substrings.add(substring)
        return list(substrings)