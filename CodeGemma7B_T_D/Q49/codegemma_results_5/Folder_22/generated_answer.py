def if_decimal_is_divisible(binary_representation):
    """
  This function checks if the decimal integer corresponding to the given binary string is divisible by the
  20th number of the Fibonacci sequence.
  """
    length = len(binary_representation)
    current_fibonacci_number = 0
    previous_fibonacci_number = 0
    for i in range(length):
        current_digit = int(binary_representation[i])
        current_fibonacci_number = previous_fibonacci_number + current_fibonacci_number
        previous_fibonacci_number = current_fibonacci_number - previous_fibonacci_number
        if current_fibonacci_number >= 20:
            if int(binary_representation, 2) % current_fibonacci_number == 0:
                return True
    return False