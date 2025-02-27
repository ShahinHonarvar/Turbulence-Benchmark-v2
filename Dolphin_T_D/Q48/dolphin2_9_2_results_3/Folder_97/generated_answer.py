def return_binary_or_hexa(nums):
    a = nums[34]
    b = nums[69]
    not_in_range = [i for i in range(a + 1, b) if i not in nums]
    return bin(sum(not_in_range)) if sum(not_in_range) % 2 == 1 else hex(sum(not_in_range)) if not_in_range else ''