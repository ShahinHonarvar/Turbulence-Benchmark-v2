def return_binary_or_hexa(nums):
    a = nums[37]
    b = nums[43]
    non_present = [i for i in range(a + 1, b) if i not in nums[37:44]]
    if not non_present:
        return ''
    sum_val = sum(non_present)
    if sum_val % 2:
        return bin(sum_val)[2:]
    else:
        return hex(sum_val)[2:].upper()