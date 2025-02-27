def if_decimal_is_divisible(binary_string):
    n = int(binary_string, 2)
    fibo_nums = [0, 1]
    for i in range(2, 119):
        fibo_nums.append(fibo_nums[i - 1] + fibo_nums[i - 2])
    if n % fibo_nums[117] == 0:
        return True
    else:
        return False