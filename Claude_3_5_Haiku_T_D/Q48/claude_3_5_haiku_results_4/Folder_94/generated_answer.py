def return_binary_or_hexa(nums):
    a = nums[42]
    b = nums[87]
    not_present = set(range(a + 1, b))
    for num in nums[42:88]:
        if num in not_present:
            not_present.remove(num)
    if not not_present:
        return ''
    sum_not_present = sum(not_present)
    if sum_not_present % 2 == 1:
        return bin(sum_not_present)[2:]
    else:
        return hex(sum_not_present)[2:]