def return_binary_or_hexa(nums):
    if len(nums) <= 79:
        return ''
    a = nums[10]
    b = nums[79]
    specified_set = set(nums[11:79])
    full_set = set(range(a + 1, b))
    missing_set = full_set - specified_set
    if not missing_set:
        return ''
    total_sum = sum(missing_set)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]