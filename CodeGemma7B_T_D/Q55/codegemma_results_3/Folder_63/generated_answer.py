from itertools import islice

def lists_with_product_equal_n(nums):

    def circular_list_product(lst):
        return lst[-1] * lst[0] * lst[1]

    def has_product_equal_n(lst, n):
        product = circular_list_product(lst)
        if product % n == 0:
            factor = product // n
            for i in range(len(lst)):
                product_of_sublist = 1
                for j in range(i, i + len(lst)):
                    product_of_sublist *= lst[j % len(lst)]
                    if product_of_sublist == factor:
                        return True
        return False
    for i in range(len(nums)):
        sublist = list(islice(nums, i, i + len(nums)))
        if has_product_equal_n(sublist, 96):
            return [sublist]
    return []