def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        if n <= 1:
            return n
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)
    for i in range(177):
        if fibonacci(i) > int(binary_str, 2):
            break
        if fibonacci(i) % int(binary_str, 2) == 0:
            return True
    return False