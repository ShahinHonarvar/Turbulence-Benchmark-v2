from collections import deque

def lists_with_product_equal_n(nums):
    n = 96
    nums = deque(nums)
    results = []
    for _ in range(len(nums)):
        product = 1
        sublist = []
        for num in nums:
            product *= num
            sublist.append(num)
            if product == n:
                results.append(sublist)
            while product > n and sublist:
                product /= sublist.pop(0)
                if product == n:
                    results.append(sublist)
        nums.rotate(-1)
    return results