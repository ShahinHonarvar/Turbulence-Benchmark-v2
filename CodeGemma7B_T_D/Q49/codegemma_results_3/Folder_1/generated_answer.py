def if_decimal_is_divisible(binary_representation):
    fn = fibonacci(90)
    if int(binary_representation, 2) % fn == 0:
        return True
    else:
        return False

def fibonacci(n):
    f0 = 0
    f1 = 1
    list_fib = [0, 1]
    for i in range(2, n):
        f2 = f0 + f1
        list_fib.append(f2)
        f0 = f1
        f1 = f2
    return list_fib[n - 1]