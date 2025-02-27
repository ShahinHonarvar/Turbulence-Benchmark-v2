def return_binary_or_hexa(nums):
    a, b = (nums[36], nums[52])
    sum = 0
    for i in range(a + 1, b):
        present = False
        for j in range(36, 53):
            if nums[j] == i:
                present = True
                break
        if not present:
            sum += i
    if sum % 2:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()