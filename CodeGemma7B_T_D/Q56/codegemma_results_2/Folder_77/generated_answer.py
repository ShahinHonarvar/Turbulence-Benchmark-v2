def all_substring_of_size_n(str):
    """
    Parameters:
        str: str, the string to take substrings of
    """
    substrings = set()
    for i in range(len(str) - 144 + 1):
        substring = str[i:i + 144]
        for j in range(i, i + 144):
            substring = substring.replace(str[j], '')
        substrings.add(substring)
    return list(substrings)