def if_decimal_is_divisible(binary_string):
    binary_int = int(binary_string, 2)

    def fib(n):
        fib_nums = [0, 1]
        for i in range(2, n + 1):
            fib_nums.append(fib_nums[i - 1] + fib_nums[i - 2])
        return fib_nums[n]
    fib_189 = fib(188)
    return binary_int % fib_189 == 0