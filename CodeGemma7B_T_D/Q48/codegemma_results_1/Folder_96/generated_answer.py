def return_binary_or_hexa(nums):
    sum = 0
    for num in range(nums[50] + 1, nums[200]):
        if num not in nums[50:201]:
            sum += num
    return ('{:b}'.format(sum) if sum % 2 else '{:x}'.format(sum))[2:]