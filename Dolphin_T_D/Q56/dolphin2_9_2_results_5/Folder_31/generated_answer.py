def all_substring_of_size_n(s):
    ss = []
    for i in range(len(s) - 45):
        ss.append(s[i:i + 46])
    unique_ss = []
    for substring in ss:
        if len(set(substring)) == len(substring):
            unique_ss.append(substring)
    return unique_ss