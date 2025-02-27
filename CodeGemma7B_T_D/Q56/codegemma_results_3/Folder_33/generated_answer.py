def all_substring_of_size_n(string):
    """
    :type string: str
    """
    substring_size = 105
    substring_set = set()
    for start in range(len(string) - substring_size + 1):
        substring = string[start:start + substring_size]
        if len(set(substring)) == substring_size:
            substring_set.add(substring)
    return list(substring_set)