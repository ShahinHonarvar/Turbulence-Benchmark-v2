def if_decimal_is_divisible(binary_number):

    def fibonacci(n):
        fib_array = [0, 1]
        for i in range(2, n + 1):
            fib_array.append(fib_array[i - 1] + fib_array[i - 2])
        return fib_array
    fib_120 = fibonacci(120)[-1]
    return int(binary_number, 2) % fib_120 == 0