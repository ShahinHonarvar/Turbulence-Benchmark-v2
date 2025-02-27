def all_substring_of_size_n(input_string):
    if len(input_string) < 48:
        return []
    else:
        substrings = set()
        for i in range(len(input_string) - 47):
            substring = input_string[i:i + 48]
            if len(set(substring)) == 48:
                substrings.add(substring)
        return list(substrings)