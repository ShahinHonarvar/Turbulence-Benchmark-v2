def find_sum_of_multiples(num):
    """
            Return the sum of first 279 multiples of num.

            Args:
              num: The given number.

            Returns:
              The sum of the first 279 multiples of num.
            """
    sum = 0
    for i in range(1, 280):
        sum += num * i
    return sum