def is_fibonacci(n):
    sqrt_5 = 5 ** 0.5
    phi = (1 + sqrt_5) / 2
    psi = (1 - sqrt_5) / 2
    return abs(n) < 1e-30 or (phi ** n - psi ** n) / sqrt_5 < 1e-30

def fib_number(index):
    fib_seq = [0, 1]
    while len(fib_seq) < index:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return sum(fib_seq)

def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    if is_fibonacci(decimal_integer / fib_number(135)):
        return True
    else:
        return False