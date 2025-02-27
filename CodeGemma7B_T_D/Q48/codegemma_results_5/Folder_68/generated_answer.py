def return_binary_or_hexa(*args):
    nums = sorted(args[0])
    a, b = (nums[0], nums[9])
    sum_absent = 0
    for i in range(a + 1, b):
        if i not in nums:
            sum_absent += i
    if sum_absent % 2 == 1:
        return bin(sum_absent)[2:]
    else:
        return hex(sum_absent)[2:].upper()