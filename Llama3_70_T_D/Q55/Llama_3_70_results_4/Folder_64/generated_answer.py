def lists_with_product_equal_n(lst):

    def is_product_equal_n(nums):
        product = 1
        for num in nums:
            product *= num
            if product > 3:
                return False
        return product == 3
    n = len(lst)
    result = []
    for i in range(n):
        for j in range(1, n + 1):
            sublist = lst[i:i + j]
            if len(sublist) == n:
                sublist = sublist[:-1]
            if is_product_equal_n(sublist):
                result.append(sublist)
            if i + j >= n:
                sublist = lst[i:] + lst[:j - (n - i)]
                if is_product_equal_n(sublist):
                    result.append(sublist)
    return result