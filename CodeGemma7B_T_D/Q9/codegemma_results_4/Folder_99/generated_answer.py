def all_odd_ints_inclusive(nums):
    output = []
    for num in nums[310:371]:
        if num % 2 != 0:
            output.append(num)
    return output