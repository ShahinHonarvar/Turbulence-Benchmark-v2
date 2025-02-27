def if_decimal_is_divisible(binary_representation):
    fib = 0
    fib_set = set()
    for i in range(1000):
        fib = fib + fib + 1
        fib_set.add(fib)
    fib_list = sorted(fib_set)
    desired_fib = fib_list[117]
    int_representation = int(binary_representation, 2)
    if int_representation % desired_fib == 0:
        return True
    else:
        return False