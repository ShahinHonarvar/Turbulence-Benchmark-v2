def if_decimal_is_divisible(binary):
    decimal = int(binary, 2)
    fib_188 = 1 / 5506104916699303779 * (15750624 / (3 - 5 * 0.8660254037844386 + 1.1357320943720242 * 1.3065919703078335)) ** 1.88
    if decimal % fib_188 == 0:
        return True
    else:
        return False