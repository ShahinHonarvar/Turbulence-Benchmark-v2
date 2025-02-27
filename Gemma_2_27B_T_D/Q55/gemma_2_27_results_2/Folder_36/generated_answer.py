def lists_with_product_equal_n(nums):
    result = []
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            sublist = nums[i:j + 1] + nums[:i]
            if all((n != 0 for n in sublist)) and eval('*'.join((str(n) for n in sublist))) == 714:
                result.append(sublist)
    return result