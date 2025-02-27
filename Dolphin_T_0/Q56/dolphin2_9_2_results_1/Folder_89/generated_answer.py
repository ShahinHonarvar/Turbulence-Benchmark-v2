def all_substring_of_size_n(S):
    if len(S) < 38:
        return []
    output = set()
    for i in range(len(S) - 37):
        substring = S[i:i + 38]
        if len(set(substring)) == 38:
            output.add(substring)
    return list(output)