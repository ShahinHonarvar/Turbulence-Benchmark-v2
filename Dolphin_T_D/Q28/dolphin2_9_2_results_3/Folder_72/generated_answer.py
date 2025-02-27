def return_nth_smallest_ascii(s):
    valid_s = [c for c in s if ord(c) in range(33, 61)]
    sorted_s = sorted(set(valid_s), key=lambda x: ord(x))
    return sorted_s[18 - 1] if len(sorted_s) >= 18 else 'No character found'