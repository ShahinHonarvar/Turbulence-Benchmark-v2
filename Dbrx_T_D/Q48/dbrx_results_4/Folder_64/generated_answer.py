def return_binary_or_hexa(nums):
    a, b = (nums[0], nums[5])
    present_nums = set(nums[:5])
    sum_of_missing = 0
    for num in range(a + 1, b):
        if num not in present_nums:
            sum_of_missing += num
    if sum_of_missing % 2:
        return bin(sum_of_missing).split('0b')[1]
    else:
        return hex(sum_of_missing).split('0x')[1].upper()