def if_decimal_is_divisible(binary):
    length = len(binary)
    n1 = 0
    n2 = 1
    third_number = n1 + n2
    fib_nums = [0, 1]
    while third_number <= 1000:
        fib_nums.append(third_number)
        n1 = n2
        n2 = third_number
        third_number = n1 + n2
    decimal = 0
    for i, bit in enumerate(binary):
        if bit == '1':
            decimal += 2 ** (length - i - 1)
    index = [i for i, num in enumerate(fib_nums) if num > decimal][0]
    return fib_nums[index] % 13 == 0