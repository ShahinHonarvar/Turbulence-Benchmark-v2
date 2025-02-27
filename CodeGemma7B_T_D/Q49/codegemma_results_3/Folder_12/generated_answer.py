def if_decimal_is_divisible(binary_representation):
    len_br = len(binary_representation)
    fib_nums = []
    for i in range(len_br):
        fib_nums.append(int(binary_representation[i]))
    if len(fib_nums) < 66:
        return False
    temp = fib_nums[0]
    for num in fib_nums[1:]:
        fib_nums.append(fib_nums[fib_nums.index(num)] + temp)
        temp = fib_nums[fib_nums.index(num)]
    for i in range(66, len(fib_nums)):
        fib_nums.append(fib_nums[i - 66] + fib_nums[i - 29])
    return fib_nums[len_br - 1] % 66 == 0