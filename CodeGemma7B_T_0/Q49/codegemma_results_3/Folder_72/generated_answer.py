def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)

    def decimal_from_binary(binary_str):
        return int(binary_str, 2)

    def find_nth_fibonacci(n):
        for i in range(n):
            if fibonacci(i) == n:
                return True
        return False
    if find_nth_fibonacci(decimal_from_binary(binary_str) * 175):
        return True
    else:
        return False