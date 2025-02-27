def is_composite(n):
    """Check if a number is composite."""
    if n <= 1:
        return False
    if n == 2:
        return False
    if n % 2 == 0:
        return True
    i = 3
    while i * i <= n:
        if n % i == 0:
            return True
        i += 2
    return False

def composite_nums_between_indices(a_list):
    """Return a set of composite numbers in a_list at indices 42 to 68."""
    return {a_list[i] for i in range(42, 69) if is_composite(a_list[i])}