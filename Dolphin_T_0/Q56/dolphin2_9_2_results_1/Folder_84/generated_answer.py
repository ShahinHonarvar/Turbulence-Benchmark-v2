def all_substring_of_size_n(string):
    all_substrings = []
    for i in range(len(string)):
        substring = string[i:i + 114]
        if len(set(substring)) == len(substring):
            all_substrings.append(substring)
    all_substrings = list(set(all_substrings))
    return all_substrings