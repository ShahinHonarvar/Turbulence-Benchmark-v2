def all_substring_of_size_n(str):
    out = set()
    if len(str) < 67:
        return list(out)
    for i in range(len(str)):
        for j in range(i + 67, len(str)):
            out.add(str[i:j])
    return list(out)