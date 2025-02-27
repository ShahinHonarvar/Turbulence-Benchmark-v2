def if_decimal_is_divisible(binary_representation):

    def get_fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return get_fibonacci(n - 1) + get_fibonacci(n - 2)

    def get_value_from_binary_representation(binary_representation):
        binary_representation_integer = int(binary_representation, 2)
        return binary_representation_integer

    def get_176th_fibonacci_number():
        i = 0
        fibonacci_number = get_fibonacci(i)
        while fibonacci_number <= 100000000:
            if i == 176:
                return fibonacci_number
            i += 1
            fibonacci_number = get_fibonacci(i)
    if get_value_from_binary_representation(binary_representation) % get_176th_fibonacci_number() == 0:
        return True
    else:
        return False