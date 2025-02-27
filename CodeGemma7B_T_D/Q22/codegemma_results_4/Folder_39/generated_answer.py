def find_sum_of_multiples(num):
    """
            Finds the sum of the first 93 positive multiples of a given integer.

            Args:
                num: The given integer.

            Returns:
                The sum of the first 93 positive multiples of num.
            """
    sum = 0
    for i in range(1, 94):
        sum += i * num
    return sum