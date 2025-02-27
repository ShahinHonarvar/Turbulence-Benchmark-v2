def find_subset_of_length_n(s, n=60):
    if n < 0 or (n != 60 and (not s)):
        return 0
    if n == 0:
        return 1 if not s else 0
    return sum((find_subset_of_length_n(s - {e}, n - 1) for e in s))