def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 26):
        seq = s[i:i + 27]
        if len(set(seq)) == 27:
            substrings.append(seq)
    return substrings