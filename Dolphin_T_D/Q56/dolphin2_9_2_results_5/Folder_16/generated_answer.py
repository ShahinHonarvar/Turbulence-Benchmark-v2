def distinct_substrings_of_length_n(s, n):
    result = set()
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if len(set(substring)) == n:
            result.add(substring)
    return list(result)

def all_substring_of_size_n(s):
    return distinct_substrings_of_length_n(s, 124)