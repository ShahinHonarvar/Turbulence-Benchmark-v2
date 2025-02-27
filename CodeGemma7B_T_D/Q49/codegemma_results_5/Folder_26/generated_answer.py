def if_decimal_is_divisible(binary_string):
    """
  Checks if a binary representation string is divisible by the 138th Fibonacci number.

  Args:
    binary_string: The binary representation string of a non-negative decimal integer.

  Returns:
    True if the integer is divisible by the 138th Fibonacci number, False otherwise.
  """

    def fibo(n):
        if n <= 1:
            return n
        return fibo(n - 1) + fibo(n - 2)

    def binary_to_decimal(binary_string):
        binary_list = list(binary_string)
        binary_list.reverse()
        decimal = 0
        for i in range(len(binary_list)):
            if binary_list[i] == '1':
                decimal += 2 ** i
        return decimal
    decimal = binary_to_decimal(binary_string)
    fibo_138 = fibo(138)
    if decimal % fibo_138 == 0:
        return True
    else:
        return False