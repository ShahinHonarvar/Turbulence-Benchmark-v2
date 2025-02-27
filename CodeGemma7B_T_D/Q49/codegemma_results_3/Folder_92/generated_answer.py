def if_decimal_is_divisible(binary_str):
    """
    Write a function called 'if_decimal_is_divisible' that takes one argument, a binary representation string of a non-negative decimal integer.
    In the given binary representation the most significant digit appears first.
    The function should return true if the decimal integer corresponding to the given string is divisible by the 7th number that occurs in the Fibonacci sequence; otherwise, it should return false.
    The first number that occurs in the Fibonacci sequence is 0.
    """

    def generate_fibonacci():
        a, b = (0, 1)
        while True:
            yield a
            a, b = (b, a + b)
    fibonacci_iterator = generate_fibonacci()
    seventh_fibonacci_number = next(fibonacci_iterator)
    seventh_fibonacci_number = next(fibonacci_iterator)
    seventh_fibonacci_number = next(fibonacci_iterator)
    seventh_fibonacci_number = next(fibonacci_iterator)
    seventh_fibonacci_number = next(fibonacci_iterator)
    seventh_fibonacci_number = next(fibonacci_iterator)
    decimal_number = int(binary_str, 2)
    return decimal_number % seventh_fibonacci_number == 0