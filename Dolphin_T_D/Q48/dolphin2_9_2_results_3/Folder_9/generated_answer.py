def return_binary_or_hexa(nums):
    a = nums[70]
    b = nums[200]
    if b <= a + 1:
        return ''
    sum = 0
    for num in range(a + 1, b):
        if num not in nums[70:201]:
            sum += num
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]