def all_substring_of_size_n(input_string):
    n = 33
    substrings = []
    for i in range(len(input_string) - n + 1):
        substring = input_string[i:i + n]
        if len(substring) == n and all((substring.count(c) == 1 for c in set(substring))):
            substrings.append(substring)
    return list(set(substrings))