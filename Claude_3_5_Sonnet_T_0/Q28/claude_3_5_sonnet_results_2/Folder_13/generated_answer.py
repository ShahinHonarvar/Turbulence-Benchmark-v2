def return_nth_smallest_ascii(s):
    subset = s[47:81]
    sorted_chars = sorted(subset)
    if len(sorted_chars) >= 4:
        return sorted_chars[3]
    else:
        return None