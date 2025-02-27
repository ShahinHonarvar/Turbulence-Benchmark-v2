def if_decimal_is_divisible(binary_rep):
    decimal_num = int(binary_rep, 2)
    fibonacci_nums = set([0, 1])
    while True:
        next_num = fibonacci_nums.pop()
        fibonacci_nums.add(next_num)
        fibonacci_nums.add(next_num + fibonacci_nums.next())
        if len(fibonacci_nums) == 28:
            break
    return decimal_num % fibonacci_nums.next() == 0