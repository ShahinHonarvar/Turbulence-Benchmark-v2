def if_decimal_is_divisible(binary):
    """
    Write a function called 'if_decimal_is_divisible' that takes one argument, a binary representation string of a non-negative decimal integer. In the given binary representation the most significant digit appears first. The function should return true if the decimal integer corresponding to the given string is divisible by the 170th number that occurs in the Fibonacci sequence; otherwise, it should return false. The first number that occurs in the Fibonacci sequence is 0.
    """

    def fibonacci(n):
        """
        Return the nth Fibonacci number.
        """
        if n <= 1:
            return n
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)

    def decimal_to_int(binary):
        """
        Convert a binary string to an integer.
        """
        return int(binary, 2)

    def is_divisible(number, divisor):
        """
        Return True if number is divisible by divisor.
        """
        return number % divisor == 0
    integer = decimal_to_int(binary)
    fibonacci_170 = fibonacci(170)
    return is_divisible(integer, fibonacci_170)