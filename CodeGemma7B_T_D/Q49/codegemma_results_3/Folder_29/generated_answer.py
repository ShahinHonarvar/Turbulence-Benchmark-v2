def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

def get_nth_fib(n):
    fib_nums = []
    for i in range(n):
        fib_nums.append(fib(i))
    return fib_nums[n - 1]

def if_decimal_is_divisible(binary):
    decimal = int(binary, 2)
    fib_num = get_nth_fib(int(binary.count('1')) + 2)
    return decimal % fib_num == 0