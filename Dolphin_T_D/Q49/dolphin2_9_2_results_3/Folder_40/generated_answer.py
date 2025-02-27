def if_decimal_is_divisible(binary):
    decimal = int(binary, 2)
    fibonacci_seq = [0, 1]
    for i in range(2, 5):
        fibonacci_seq.append(fibonacci_seq[i - 1] + fibonacci_seq[i - 2])
    fourth_num_in_fibonacci = fibonacci_seq[3]
    return decimal % fourth_num_in_fibonacci == 0