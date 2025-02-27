def return_n_smallest_chars(s):
    return sorted([char for char in s for _ in range(52 // len(s) + (1 if 52 % len(s) > 0 else 0))][:52], reverse=True)