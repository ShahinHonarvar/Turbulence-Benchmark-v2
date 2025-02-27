def if_decimal_is_divisible(binary_str):

    def fib(no):
        if no <= 1:
            return no
        return fib(no - 1) + fib(no - 2)
    binary_hex = int(binary_str, 2)
    index = 10
    while True:
        fib_no = fib(index)
        if fib_no > binary_hex * 178:
            break
        index += 1
    if fib_no % binary_hex == 0:
        return True
    return False