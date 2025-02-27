def return_nth_smallest_ascii(s):
    chars = sorted(set((s[i] for i in range(5))))
    if len(chars) < 5:
        return None
    return chr(chars[4])