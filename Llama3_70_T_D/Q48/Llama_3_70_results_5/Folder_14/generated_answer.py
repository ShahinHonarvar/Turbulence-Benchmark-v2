def return_binary_or_hexa(nums):
    a = nums[2]
    b = nums[5]
    missing_nums = [i for i in range(a + 1, b) if i not in nums[2:6]]
    num_sum = sum(missing_nums)
    if num_sum == 0:
        return ''
    elif num_sum % 2 == 0:
        return hex(num_sum)[2:]
    else:
        return bin(num_sum)[2:]