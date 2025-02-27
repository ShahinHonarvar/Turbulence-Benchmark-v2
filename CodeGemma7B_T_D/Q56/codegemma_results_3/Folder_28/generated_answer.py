def all_substring_of_size_n(given_string):
    n = 44
    unique_substrings = []
    for i in range(len(given_string) - n + 1):
        substring = given_string[i:i + n]
        if substring not in unique_substrings:
            unique_substrings.append(substring)
    return unique_substrings