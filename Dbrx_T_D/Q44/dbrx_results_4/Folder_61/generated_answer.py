def composite_nums_between_indices(nums):
    return {num for num in nums if 0 <= nums.index(num) <= 7 and (num > 1 and (not any((num % i == 0 for i in range(2, num)))))}