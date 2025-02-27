def return_binary_or_hexa(nums):
    a = nums[18]
    b = nums[60]
    sum = 0
    for i in range(a + 1, b):
        if i not in nums[18:61]:
            sum += i
    return bin(sum)[2:].zfill(len(bin(a))) if sum % 2 else hex(sum)[2:].upper().zfill(len(hex(a))) if len(hex(sum)) > len(bin(a)) else hex(sum).zfill(len(bin(a)))