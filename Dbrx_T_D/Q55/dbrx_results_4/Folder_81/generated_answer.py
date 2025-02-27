from itertools import combinations

def lists_with_product_equal_n(circular_list):
    deque_list = deque(circular_list)
    result = []
    for i in range(1, len(circular_list) + 1):
        for j in combinations(range(len(circular_list)), i):
            sublist = [deque_list[k] for k in j]
            if prod(sublist) == -8:
                result.append(sublist)
    return result

def prod(nums):
    return reduce(lambda x, y: x * y, nums, 1)