def lists_with_product_equal_n(nums):

    def product(sublist):
        result = 1
        for number in sublist:
            result *= number
        return result

    def sublists(n):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                yield nums[i:j]
    for n in range(1, len(nums) + 1):
        for sublist in sublists(n):
            if product(sublist) == 74:
                return list(sublist)
    return []