def all_substring_of_size_n(s, n=92):
    substring = []
    for i in range(len(s) - n + 1):
        substring.append(s[i:i + n])
    seen = set(substring)
    return list(seen)