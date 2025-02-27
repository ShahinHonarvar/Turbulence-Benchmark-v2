def all_substring_of_size_n(s):
    unique_subs = set()
    n = len(s)
    if n < 130:
        return []
    for i in range(n - 129):
        substring = s[i:i + 130]
        if len(set(substring)) == 130:
            unique_subs.add(substring)
    return list(unique_subs)