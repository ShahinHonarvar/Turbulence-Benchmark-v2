def return_nth_smallest_ascii(s):
    if len(s) < 18:
        return None
    return sorted(s[:18])[17]