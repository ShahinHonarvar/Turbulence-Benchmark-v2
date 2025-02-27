def return_binary_or_hexa(nums):
    present = [False] * (max(nums) + 1)
    for num in nums:
        present[num] = True
    a = nums[10]
    b = nums[76]
    sum_missing = 0
    for i in range(a + 1, b):
        if not present[i]:
            sum_missing += i
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    return hex(sum_missing)[2:].upper() if sum_missing else ''