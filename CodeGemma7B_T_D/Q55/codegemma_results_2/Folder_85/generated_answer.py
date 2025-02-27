from itertools import combinations

def lists_with_product_equal_n(nums):
    circular_nums = nums + [nums[0]]
    sublists = []
    for i in range(len(circular_nums)):
        for j in range(i + 1, len(circular_nums)):
            product = 1
            for num in circular_nums[i:j]:
                product *= num
            if product == -97 and [circular_nums[i:j]] not in sublists:
                sublists.append([circular_nums[i:j]])
    return sublists