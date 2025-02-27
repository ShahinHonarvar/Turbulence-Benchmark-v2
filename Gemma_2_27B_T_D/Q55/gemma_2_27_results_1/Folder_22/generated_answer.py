def lists_with_product_equal_n(nums):
    result = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + 1):
            sublist = nums[i:j]
            if len(sublist) <= len(nums) and all((isinstance(x, int) for x in sublist)) and (prod(sublist) == 4):
                result.append(sublist)
    return result

def prod(iterable):
    p = 1
    for n in iterable:
        p *= n
    return p