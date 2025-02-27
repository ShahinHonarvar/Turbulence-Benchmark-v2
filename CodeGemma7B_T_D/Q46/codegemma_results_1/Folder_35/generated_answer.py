def gcf_three_nums(num_list):
    """
    This functions takes a list of positive integers and returns the GCF of the elements at indices 742, 888 and 629
    """
    num_1 = num_list[742]
    num_2 = num_list[888]
    num_3 = num_list[629]
    result = math.gcd(math.gcd(num_1, num_2), num_3)
    return result