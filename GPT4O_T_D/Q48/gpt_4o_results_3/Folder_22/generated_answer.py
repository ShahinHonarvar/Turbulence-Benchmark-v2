def return_binary_or_hexa(nums):
    a = nums[40]
    b = nums[200]
    sum_missing = 0
    current = a + 1
    idx = 41
    while idx < 200 and current < b:
        if nums[idx] != current:
            sum_missing += current
            current += 1
        else:
            current += 1
            idx += 1
    while current < b:
        sum_missing += current
        current += 1
    if sum_missing == 0:
        return ''
    if sum_missing % 2 == 0:
        return format(sum_missing, 'x')
    else:
        return format(sum_missing, 'b')