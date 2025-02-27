def all_substring_of_size_n(string):
    substrs = set()
    for i in range(len(string) - 33):
        substring = string[i:i + 34]
        if len(set(substring)) == 34:
            substrs.add(substring)
    return list(substrs)