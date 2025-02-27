def return_n_smallest_chars(s):
    return sorted([c for c in s if ord(c) in sorted(set(map(ord, s)))[:26]], reverse=True)