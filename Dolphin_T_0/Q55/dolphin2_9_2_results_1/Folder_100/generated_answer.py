def lists_with_product_equal_n(nums):

    def get_sublists(nums):
        n = len(nums)
        sublists = []
        for i in range(n):
            product = 1
            for j in range(i, n):
                product *= nums[j]
                if product == 48:
                    sublists.append(nums[i:j + 1])
        return sublists

    def get_circular_sublists(i, n):
        product = 1
        sublists = []
        for j in range(i, i + n):
            product *= nums[j % n]
            if product == 48:
                sublists.append(nums[i:j + 1])
        return sublists
    result = []
    n = len(nums)
    if n == 1:
        return result
    forward = get_sublists(nums)
    for i in range(n):
        temp_nums = nums[i + 1:] + nums[:i + 1]
        backward = get_circular_sublists(i, n - 1)
        result.extend(forward + backward)
        for sublist in forward:
            if sublist[0] == sublist[-1]:
                result.extend([temp_nums[j:j + len(sublist - 1)] + [temp_nums[0]] for j in range(len(sublist - 1))])
    return result