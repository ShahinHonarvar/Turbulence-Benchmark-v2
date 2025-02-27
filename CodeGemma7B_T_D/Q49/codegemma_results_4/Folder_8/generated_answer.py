def if_decimal_is_divisible(binary_representation):

    def is_valid_binary(binary):
        for char in binary:
            if char not in ('0', '1'):
                return False
        return True

    def calculate_fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            return calculate_fibonacci(n - 1) + calculate_fibonacci(n - 2)

    def get_nth_fibonacci(binary):
        binary_number = int(binary, 2)
        next_fibonacci = calculate_fibonacci(binary_number)
        return int(next_fibonacci / 54)
    if not is_valid_binary(binary_representation):
        return False
    Nth_fibonacci_number = get_nth_fibonacci(binary_representation)
    if Nth_fibonacci_number == int(Nth_fibonacci_number):
        return True
    else:
        return False