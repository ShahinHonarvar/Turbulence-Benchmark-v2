def return_nth_smallest_ascii(s):
    eligible = sorted([ch for ch in s if 32 <= ord(ch) <= 67])
    if len(eligible) >= 12:
        return eligible[11]
    else:
        return None