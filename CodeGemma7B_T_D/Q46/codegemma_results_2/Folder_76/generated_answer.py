def gcf_three_nums(lst):
    """Calculates the greatest common factor of the elements at indices 876, 203 and 100 in a list."""
    min_num = min(lst[876], lst[203], lst[100])
    gcd = min_num
    for num in [lst[876], lst[203], lst[100]]:
        if num % gcd != 0:
            gcd = num % gcd
    return gcd