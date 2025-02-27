def all_substring_of_size_n(str):
    """
                This function generates all distinct substrings of a given string with a length of n.
            
                Args:
                str: The input string.
            
                Returns:
                A list of all distinct substrings of length n, or an empty list if no such substrings exist.
            """
    all_distinct_substring_of_n = set()
    n = 96
    for i in range(len(str) - n + 1):
        substring = str[i:i + n]
        all_distinct_substring_of_n.add(substring)
    return list(all_distinct_substring_of_n)