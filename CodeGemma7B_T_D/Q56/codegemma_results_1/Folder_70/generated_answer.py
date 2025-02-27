def all_substring_of_size_n(string):
    all_str = set()
    for i in range(len(string) - 11):
        all_str.add(string[i:i + 12])
    return list(all_str)