def if_decimal_is_divisible(binary_rep_string):
    decimal = int(binary_rep_string, 2)
    fibonacci_84th = [0, 1]
    for i in range(2, 85):
        fibonacci_84th.append(fibonacci_84th[i - 1] + fibonacci_84th[i - 2])
    return decimal % fibonacci_84th[-1] == 0