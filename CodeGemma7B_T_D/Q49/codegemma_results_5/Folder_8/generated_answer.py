def if_decimal_is_divisible(binary_representation):
    binary_length = len(binary_representation)
    fibonacci_list = [0, 1]
    a = fibonacci_list[-2]
    b = fibonacci_list[-1]
    nth_fibonacci = 54
    for i in range(2, nth_fibonacci):
        c = a + b
        fibonacci_list.append(c)
        a, b = (b, c)
    mask = 2 ** (nth_fibonacci - 1)
    referenced_digit = fibonacci_list[-1] & mask
    binary_representation_int = int(binary_representation, 2)
    return binary_representation_int % referenced_digit == 0