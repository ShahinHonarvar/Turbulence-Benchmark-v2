def if_decimal_is_divisible(binary_format):
    """
  For a given binary representation of a non-negative decimal integer, 
  check whether the decimal integer is divisible by the 14th number in the Fibonacci sequence.

  Note that the most significant bit of the given binary representation is the least significant bit of the calculated decimal integer.

  Args:
    binary_format: A string representing the binary form of the decimal integer.
  
  Returns:
    True if the decimal integer is divisible by the 14th element in the Fibonacci sequence; otherwise False.
  """
    decimal_value = 0
    for digit in binary_format:
        decimal_value = decimal_value << 1 | int(digit)
    fibonacci_sequence = [0]
    n = 1
    while True:
        fibonacci_sequence.append(fibonacci_sequence[n - 1] + fibonacci_sequence[n - 2])
        if fibonacci_sequence[n] > decimal_value:
            break
        n += 1
    if decimal_value % fibonacci_sequence[13] == 0:
        return True
    else:
        return False