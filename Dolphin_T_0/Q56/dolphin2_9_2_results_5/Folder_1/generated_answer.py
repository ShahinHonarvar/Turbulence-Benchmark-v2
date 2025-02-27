def all_substring_of_size_n(s):
    subs = set()
    for i in range(len(s) - 23):
        substring = s[i:i + 24]
        if len(set(substring)) == len(substring):
            subs.add(substring)
    return list(subs)