def if_decimal_is_divisible(binary_representation):

    def binary_to_decimal(binary_representation):
        decimal_representation = 0
        for digit in binary_representation:
            decimal_representation = decimal_representation * 2 + int(digit)
        return decimal_representation

    def find_nth_fibonacci_number(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            return find_nth_fibonacci_number(n - 1) + find_nth_fibonacci_number(n - 2)
    decimal_representation = binary_to_decimal(binary_representation)
    fib_number = find_nth_fibonacci_number(9)
    return decimal_representation % fib_number == 0