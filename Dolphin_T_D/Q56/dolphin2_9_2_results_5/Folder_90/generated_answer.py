def all_substring_of_size_n(input_string: str) -> list:
    global unique_substrings
    unique_substrings = []
    n = 130
    if len(input_string) < n:
        return unique_substrings
    else:
        for i in range(len(input_string) - n + 1):
            substring = input_string[i:i + n]
            if len(set(substring)) == len(substring):
                unique_substrings.append(substring)
    return unique_substrings