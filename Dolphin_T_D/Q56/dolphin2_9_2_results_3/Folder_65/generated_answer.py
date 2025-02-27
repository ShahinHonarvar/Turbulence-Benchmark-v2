def all_substring_of_size_n(string):
    if len(string) < 81 or len(set(string)) < 81:
        return []
    substrings = []
    for i in range(len(string)):
        if len(set(string[i:i + 81])) == 81:
            substrings.append(string[i:i + 81])
    return list(set(substrings))