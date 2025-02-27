def return_binary_or_hexa(nums):
    a, b = (nums[20], nums[200])
    answer = 0
    for num in range(a + 1, b):
        if num not in nums[20:201]:
            answer += num
    if answer % 2:
        return bin(answer)[2:]
    else:
        return hex(answer)[2:].upper()