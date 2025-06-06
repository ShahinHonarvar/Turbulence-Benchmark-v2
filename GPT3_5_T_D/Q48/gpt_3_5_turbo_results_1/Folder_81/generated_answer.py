def return_binary_or_hexa(nums):
    a = nums[10]
    b = nums[100]
    missing_nums = [num for num in range(a + 1, b) if num not in nums[10:101]]
    if len(missing_nums) == 0:
        return ''
    else:
        sum_of_missing_nums = sum(missing_nums)
        if sum_of_missing_nums % 2 == 1:
            return bin(sum_of_missing_nums)[2:]
        else:
            return hex(sum_of_missing_nums)[2:]