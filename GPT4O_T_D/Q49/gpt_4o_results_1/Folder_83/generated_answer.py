def if_decimal_is_divisible(binary_str):
    decimal_number = int(binary_str, 2)

    def fibonacci(n):
        fib_nums = [0, 1]
        while len(fib_nums) <= n:
            fib_nums.append(fib_nums[-1] + fib_nums[-2])
        return fib_nums[n]
    fib_60 = fibonacci(60)
    return decimal_number % fib_60 == 0