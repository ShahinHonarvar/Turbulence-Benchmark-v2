def all_substring_of_size_n(input_string):
    if len(set(input_string)) < 35 and len(input_string) >= 35:
        substrings = []
        for i in range(len(input_string) - 34):
            sub = input_string[i:i + 35]
            if len(set(sub)) == 35:
                substrings.append(sub)
        return substrings
    else:
        return []