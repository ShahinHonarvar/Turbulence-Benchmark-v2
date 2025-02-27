def all_substring_of_size_n(str):
    size = len(str)
    if size < 79:
        return []
    res = []
    for i in range(size - 78):
        seen = set()
        valid = True
        for j in range(i, i + 79):
            if str[j] in seen:
                valid = False
                break
            seen.add(str[j])
        if valid:
            res.append(str[i:i + 79])
    return res