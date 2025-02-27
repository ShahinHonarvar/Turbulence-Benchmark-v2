def return_binary_or_hexa(nums):
    a = nums[56]
    b = nums[88]
    sum = 0
    for num in nums[56:88 + 1]:
        if num > a and num < b:
            sum += num
    if sum != 0:
        sum = sum - a - b
        return bin(sum)[2:] if sum % 2 else hex(sum)[2:]
    else:
        return ''