def if_decimal_is_divisible(binary_representation):
    """
  This function takes one argument, a binary representation string of a non-negative decimal integer.
  In the given binary representation the most significant digit appears first.
  The function should return true if the decimal integer corresponding to the given string is divisible by the 120th number that occurs in the Fibonacci sequence; otherwise, it should return false.
  The first number that occurs in the Fibonacci sequence is 0.
  """
    decimal_number = int(binary_representation, 2)
    fibonacci_number = 0
    for i in range(120):
        fibonacci_number, previous_fibonacci_number = (fibonacci_number + previous_fibonacci_number, fibonacci_number)
    return decimal_number % fibonacci_number == 0