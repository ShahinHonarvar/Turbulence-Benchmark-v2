def return_nth_smallest_ascii(s):
    filtered = [s[i] for i in range(14, 67) if 0 <= i < len(s)]
    filtered.sort(key=lambda x: ord(x))
    if len(filtered) >= 8:
        return filtered[7]
    else:
        return None