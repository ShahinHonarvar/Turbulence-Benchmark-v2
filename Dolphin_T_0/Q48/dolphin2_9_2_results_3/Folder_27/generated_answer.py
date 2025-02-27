def return_binary_or_hexa(nums):
    a = nums[86]
    b = nums[89]
    present_nums = [num for num in nums if num >= a and num <= b]
    missing_nums_sum = sum((num for num in range(a, b + 1) if num not in present_nums))
    if missing_nums_sum % 2 == 1:
        return bin(missing_nums_sum)[2:]
    else:
        return hex(missing_nums_sum)[2:]