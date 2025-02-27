def return_n_smallest_chars(s):
    s = [char for char in s if char.isalpha()]
    s.sort(key=lambda x: x.lower())
    return sorted(s[:26])[::-1]