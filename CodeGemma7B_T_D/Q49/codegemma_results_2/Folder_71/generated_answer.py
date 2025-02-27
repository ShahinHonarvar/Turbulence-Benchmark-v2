def if_decimal_is_divisible(binary_str):
    bin_value = int(binary_str, 2)
    fib_num = generate_fibonacci_num(147)
    return bin_value % fib_num == 0

def generate_fibonacci_num(num):
    fib_list = [0, 1]
    for i in range(2, num):
        fib_list.append(fib_list[i - 2] + fib_list[i - 1])
    return fib_list[num - 1]