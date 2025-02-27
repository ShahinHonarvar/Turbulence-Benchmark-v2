def all_substring_of_size_n(input_string):
    if len(input_string) < 74:
        return []
    start = 0
    end = 74
    substrings = []
    while end <= len(input_string):
        substring = input_string[start:end]
        if len(set(substring)) == len(substring):
            substrings.append(substring)
        start += 1
        end += 1
    return substrings