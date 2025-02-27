def return_nth_smallest_ascii(s):
    return sorted(s[:18])[17] if len(s) >= 18 else None