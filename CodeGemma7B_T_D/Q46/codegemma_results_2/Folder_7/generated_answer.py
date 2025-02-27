def gcf_three_nums(a):
    """
    The function takes one argument, a list of positive integers,
    and returns the greatest common factor of the elements at indices 477, 696 and 663.
    """
    first_number = a[477]
    second_number = a[696]
    third_number = a[663]
    while first_number != second_number:
        if first_number > second_number:
            first_number -= second_number
        else:
            second_number -= first_number
    gcd = first_number
    while gcd != third_number:
        if gcd > third_number:
            gcd -= third_number
        else:
            third_number -= gcd
    return gcd