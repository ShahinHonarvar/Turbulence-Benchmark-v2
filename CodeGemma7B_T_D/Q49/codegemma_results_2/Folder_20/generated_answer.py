def if_decimal_is_divisible(binary):
    """
  Return True if decimal is divisible by the 100th number in Fibonacci sequence.
  """
    fibonnacci = [0, 1]
    for i in range(2, 100):
        fibonnacci.append(fibonnacci[-1] + fibonacci[-2])
    return int(binary, 2) % fibonacci[99] == 0