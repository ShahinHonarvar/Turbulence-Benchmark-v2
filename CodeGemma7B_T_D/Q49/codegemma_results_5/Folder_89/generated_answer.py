def if_decimal_is_divisible(binary_representation):
    """
  This function checks if the decimal integer corresponding to the given binary representation is divisible by the 126th number that occurs in the Fibonacci sequence.

  Args:
    binary_representation: A string representing the binary representation of a non-negative decimal integer.

  Returns:
    True if the decimal integer is divisible by the 126th Fibonacci number, False otherwise.
  """
    decimal_integer = int(binary_representation, 2)
    fibonacci_value = fibonacci(126)
    if decimal_integer % fibonacci_value == 0:
        return True
    else:
        return False

def fibonacci(index):
    """
  This function calculates the Fibonacci number at the given index.

  Args:
    index: The index of the Fibonacci number to calculate.

  Returns:
    The Fibonacci number at the given index.
  """
    if index == 0:
        return 0
    elif index == 1:
        return 1
    else:
        return fibonacci(index - 1) + fibonacci(index - 2)