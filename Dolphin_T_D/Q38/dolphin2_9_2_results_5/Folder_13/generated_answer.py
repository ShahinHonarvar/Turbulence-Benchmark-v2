def find_subset_of_length_n(s):
    if len(s) < 801:
        return 0
    count = 1
    for i in range(len(s) - 801):
        substr = s[i:i + 801]
        count += 1 if set(substr).issubset(s) else 0
    return count