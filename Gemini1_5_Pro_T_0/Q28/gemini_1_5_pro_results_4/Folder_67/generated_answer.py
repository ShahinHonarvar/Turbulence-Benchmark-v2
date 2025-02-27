def return_nth_smallest_ascii(s):
    return sorted([ord(s[i]) for i in range(max(60, len(s)), min(84, len(s) + 1))])[13] if len(s) >= 74 else -1