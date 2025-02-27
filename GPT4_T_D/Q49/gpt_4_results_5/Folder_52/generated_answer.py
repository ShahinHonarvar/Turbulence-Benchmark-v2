def if_decimal_is_divisible(bin_str):

    def nthFibonacci(n):
        a, b = (0, 1)
        for i in range(n):
            a, b = (b, a + b)
        return a
    decimal = int(bin_str, 2)
    nth_fib = nthFibonacci(176)
    return decimal % nth_fib == 0