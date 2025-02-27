from itertools import islice, cycle

def lists_with_product_equal_n(nums):
    target = 48
    result = []
    for i in range(len(nums)):
        window = list(islice(cycle(nums[i:]), i + 1))
        prod = 1
        sub_list = []
        for num in window:
            prod *= num
            sub_list.append(num)
            if prod == target:
                result.append(sub_list.copy())
            elif prod > target:
                break
    return result