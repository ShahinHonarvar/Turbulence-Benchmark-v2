def if_decimal_is_divisible(binary_str):
    """
            Takes a binary representation string of a non-negative decimal integer as an argument,
            the most significant digit appearing first.
            Returns true if the decimal integer corresponding to the given string is divisible by the 84th number
            that occurs in the Fibonacci sequence; otherwise, it returns false.
            The first number that occurs in the Fibonacci sequence is 0.
            """

    def is_bin_divisible_by_num(binary_str, num):
        """
                Checks if a binary number is divisible by a number.
                """
        decimal_num = int(binary_str, 2)
        return decimal_num % num == 0

    def get_fibo_num(index):
        """
                Returns the Fibonacci number at the given index,
                the first Fibonacci number being at index 0.
                """
        if index < 2:
            return index
        else:
            return get_fibo_num(index - 1) + get_fibo_num(index - 2)
    fibo_84 = get_fibo_num(84)
    return is_bin_divisible_by_num(binary_str, fibo_84)