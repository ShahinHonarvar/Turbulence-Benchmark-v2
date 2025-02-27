def lists_with_product_equal_n(nums):
    sublists = []
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            sublist = nums[i:j + 1] + nums[:i] if j >= i else nums[i:]
            if -89 in [product for product in [num for num in [1] + [n1 * n2 for n1, n2 in zip(sublist, sublist[1:])] for num in [1] + [n1 * n2 for n1, n2 in zip(num, num[1:])]]]:
                sublists.append(sublist)
    return sublists