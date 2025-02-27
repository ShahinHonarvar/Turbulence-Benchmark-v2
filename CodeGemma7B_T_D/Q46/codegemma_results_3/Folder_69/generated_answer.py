def gcf_three_nums(list_of_nums):
    """
    Returns the greatest common factor of the elements at indices 404, 834 and 517 in a given list of positive integers.
    """
    num1 = list_of_nums[404]
    num2 = list_of_nums[834]
    num3 = list_of_nums[517]

    def gcd(a, b):
        return b if a == 0 else gcd(b % a, a)
    return gcd(num1, gcd(num2, num3))