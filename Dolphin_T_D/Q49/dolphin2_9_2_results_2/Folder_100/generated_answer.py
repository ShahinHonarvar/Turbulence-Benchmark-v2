def if_decimal_is_divisible(binary_string):
    n = len(binary_string)
    decimal = 0
    for i in range(n):
        decimal += int(binary_string[n - 1 - i]) * 2 ** i
    fibonacci_seq = [0, 1]
    while len(fibonacci_seq) < 190:
        fibonacci_seq.append(fibonacci_seq[-1] + fibonacci_seq[-2])
    if fibonacci_seq[189] != 0 and decimal % fibonacci_seq[189] == 0:
        return True
    return False