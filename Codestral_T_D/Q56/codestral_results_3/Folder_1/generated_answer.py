def all_substring_of_size_n(input_string):
    if len(input_string) < 24:
        return []
    else:
        result = []
        for i in range(len(input_string) - 23):
            substring = input_string[i:i + 24]
            if len(set(substring)) == 24:
                result.append(substring)
        return result