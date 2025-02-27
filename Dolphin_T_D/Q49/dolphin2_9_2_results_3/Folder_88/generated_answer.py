def if_decimal_is_divisible(binary_str):
    decimal_num = int(binary_str, 2)
    fibonacci_seq = [0, 1]
    for i in range(2, 49):
        fibonacci_seq.append(fibonacci_seq[i - 1] + fibonacci_seq[i - 2])
    return decimal_num % fibonacci_seq[-1] == 0