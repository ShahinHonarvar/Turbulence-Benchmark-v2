from itertools import islice, combinations

def lists_with_product_equal_n(nums):
    circular_nums = nums + [nums[0]]
    result = []

    def product(sublist):
        return sum((circular_nums[i:i + len(sublist)] == sublist for i in range(len(circular_nums) - len(sublist) + 1)))
    for sublist in combinations(range(len(circular_nums)), 2):
        if product(sublist) * circular_nums[sublist[1]] == -906:
            result.append(circular_nums[sublist[0]:sublist[1] + 1])
        if product(sublist[::-1]) * circular_nums[sublist[0]] == -906:
            result.append(circular_nums[sublist[1]:sublist[0] + 1])
    return result