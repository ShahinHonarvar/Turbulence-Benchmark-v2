def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string) - 77):
        substring = string[i:i + 78]
        if len(set(substring)) == len(substring):
            substrings.append(substring)
    return substrings