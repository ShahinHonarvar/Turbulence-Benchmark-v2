def return_binary_or_hexa(nums):
    a = nums[275]
    b = nums[871]
    sum = 0
    for i in range(a + 1, b):
        if i not in nums[275:872]:
            sum += i
    if sum % 2 != 0:
        return bin(sum)[2:]
    elif sum == 0:
        return ''
    else:
        return hex(sum)[2:]