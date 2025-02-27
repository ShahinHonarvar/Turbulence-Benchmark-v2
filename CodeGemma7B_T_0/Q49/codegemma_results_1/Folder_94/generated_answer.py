def if_decimal_is_divisible(binary):

    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)

    def get_nth_fibonacci(n):
        if n < 0:
            return None
        else:
            return fibonacci(n)

    def get_decimal(binary):
        decimal = 0
        for i in range(len(binary)):
            if binary[i] == '1':
                decimal += 2 ** i
        return decimal
    if get_decimal(binary) % get_nth_fibonacci(40) == 0:
        return True
    else:
        return False