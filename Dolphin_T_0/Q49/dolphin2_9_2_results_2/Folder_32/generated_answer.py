def if_decimal_is_divisible(binary_string):

    def compute_fibonacci(n):
        fibonacci = [0, 1]
        for i in range(2, n + 1):
            fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
        return fibonacci
    fibonacci_list = compute_fibonacci(178)
    return int(binary_string, 2) % fibonacci_list[177] == 0