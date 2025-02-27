def return_nth_smallest_ascii(s):
    sub_string = s[:18]
    sorted_sub = sorted(sub_string)
    return sorted_sub[17] if len(sorted_sub) >= 18 else None