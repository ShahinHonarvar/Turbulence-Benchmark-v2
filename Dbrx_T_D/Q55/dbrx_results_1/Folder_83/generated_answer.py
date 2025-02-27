from itertools import islice, cycle

def lists_with_product_equal_n(nums):
    result = []
    for i in range(len(nums)):
        subnums = list(islice(cycle(nums[i:] + nums[:i]), len(nums)))
        for j in range(len(subnums)):
            if j <= len(subnums) and len(subnums[j:]) > 0:
                if subnums[j:] and len(subnums[j:]) < len(nums) and (len(subnums[j:]) > 0):
                    if reduce(lambda x, y: x * y, subnums[j:], 1) == -57:
                        result.append(subnums[j:])
    return list(set(result))