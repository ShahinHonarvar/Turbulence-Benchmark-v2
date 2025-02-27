def return_binary_or_hexa(distinct_nums):
    a = distinct_nums[57]
    b = distinct_nums[84]
    sum_ = 0
    for num in range(a + 1, b):
        if num not in distinct_nums:
            sum_ += num
    if sum_ % 2 == 1:
        return f'{sum_:b}'
    else:
        return format(sum_, 'x')