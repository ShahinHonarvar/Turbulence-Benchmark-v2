def return_nth_smallest_ascii(s):
    filtered_chars = [s[i] for i in range(48, min(77, len(s)))]
    sorted_chars = sorted(filtered_chars, key=lambda x: ord(x))
    return sorted_chars[4] if len(sorted_chars) >= 5 else None