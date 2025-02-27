def return_n_smallest_chars(text):
    return sorted([c for c in text if ord(c) in sorted(set((ord(x) for x in text)))[:26]], reverse=True)