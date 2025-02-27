def all_substring_of_size_n(s):
    length = 37
    sb = set()
    for i in range(len(s) - length + 1):
        if len(set(s[i:i + length])) == length:
            sb.add(s[i:i + length])
    return list(sb)