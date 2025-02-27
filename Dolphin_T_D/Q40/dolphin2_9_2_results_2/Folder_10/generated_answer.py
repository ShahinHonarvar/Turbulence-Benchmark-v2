def return_n_smallest_chars(s):
    chars = [c for c in s if c not in ' ~`!@#$%^&*()-_+={}[]:;"<_{(|)>},./?\\\\| ']
    return sorted(chars, key=lambda c: ord(c), reverse=True)[:88]