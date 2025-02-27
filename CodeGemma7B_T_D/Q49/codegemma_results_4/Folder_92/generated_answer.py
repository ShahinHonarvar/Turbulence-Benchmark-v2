def if_decimal_is_divisible(binary_representation_string):
    """
    Write a function called 'if_decimal_is_divisible' that takes one argument, a binary representation string of a non-negative decimal integer.
    In the given binary representation the most significant digit appears first.
    The function should return true if the decimal integer corresponding to the given string is divisible by the 7th number that occurs in the Fibonacci sequence; otherwise, it should return false.
    The first number that occurs in the Fibonacci sequence is 0.
    """
    int_representation_of_number = int(binary_representation_string, 2)
    fibonacci_list = [0, 1]
    for i in range(2, 40):
        fibonacci_list.append(fibonacci_list[i - 1] + fibonacci_list[i - 2])
    if int_representation_of_number % fibonacci_list[6] == 0:
        return True
    else:
        return False