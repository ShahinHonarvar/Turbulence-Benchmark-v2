from itertools import cycle

def lists_with_product_equal_n(nums):
    check = 1
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            p = 1
            for v in nums[i:j + 1]:
                p *= v
            if p == check:
                for _ in range(j + 1 - i):
                    nums.append(nums.pop(0))
                return [nums[i:j + 1]]