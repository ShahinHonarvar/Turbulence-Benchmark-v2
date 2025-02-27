def if_decimal_is_divisible(binary_representation):
    fib_nums = []
    fib_nums.append(0)
    fib_nums.append(1)
    for i in range(2, 128):
        fib_nums.append(fib_nums[i - 2] + fib_nums[i - 1])
    decimal_representation = int(binary_representation, 2)
    for num in fib_nums:
        if decimal_representation % num == 0:
            return True
        elif num == fib_nums[-1]:
            return False