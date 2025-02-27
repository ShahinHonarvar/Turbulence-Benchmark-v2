def return_binary_or_hexa(nums):
    a = nums[70]
    b = nums[200]
    total_sum = sum((i for i in range(a + 1, b) if i not in nums[71:200]))
    if total_sum == 0:
        return ''
    if total_sum % 2 == 1:
        return '{0:b}'.format(total_sum)
    else:
        return '{0:x}'.format(total_sum)