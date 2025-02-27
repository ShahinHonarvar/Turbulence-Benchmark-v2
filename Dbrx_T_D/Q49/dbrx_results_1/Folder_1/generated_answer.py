def if_decimal_is_divisible(bin_rep_str):
    decimal_num = int(bin_rep_str, 2)
    fibonacci_num = fibonacci_n(90)
    if decimal_num % fibonacci_num == 0:
        return True
    else:
        return False

def fibonacci_n(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])
    return fib_sequence[-1]