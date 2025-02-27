def return_binary_or_hexa(nums):
    a = nums[10]
    b = nums[97]
    summ = 0
    for num in range(a + 1, b):
        if num not in nums[10:98]:
            summ += num
    return bin(summ)[2:] if summ % 2 else hex(summ)[2:].upper()