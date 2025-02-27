def find_divisors_in_range(a):
    """Function to find all positive divisors of a given number in the range 3-7"""
    c = []
    for i in range(3, a + 1, 1):
        if a % i != 0:
            continue
        c.append(i)
    return c