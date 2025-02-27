def is_binary_divisible_by_199th_fibonacci(binary_str):
    decimal = int(binary_str, 2)
    fibo_199 = [0, 1]
    a, b = (0, 1)
    for _ in range(2, 199):
        a, b = (b, a + b)
        fibo_199.append(b)
    return decimal % fibo_199[-1] == 0