def all_substring_of_size_n(str):
    seen, out = (set(), set())
    for i in range(len(str)):
        for j in range(i + 15, len(str) + 1):
            substring = str[i:j]
            if len(substring) == len(set(substring)):
                seen.add(substring)
    return list(seen)