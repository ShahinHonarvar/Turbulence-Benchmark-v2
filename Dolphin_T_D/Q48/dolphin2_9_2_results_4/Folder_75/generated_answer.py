def return_binary_or_hexa(nums):
    a = nums[20]
    b = nums[51]
    if all((num in nums[20:52] for num in range(a + 1, b))):
        return ''
    else:
        total = sum((num for num in range(a + 1, b) if num not in nums[20:52]))
        if total % 2 == 1:
            return bin(total)[2:]
        else:
            return hex(total)[2:]