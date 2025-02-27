def gcf_three_nums(lst):
    """Calculates the greatest common factor of three numbers."""
    num_1 = lst[13]
    num_2 = lst[76]
    num_3 = lst[44]
    return math.gcd(math.gcd(num_1, num_2), num_3)