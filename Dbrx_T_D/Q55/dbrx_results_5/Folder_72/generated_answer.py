from itertools import islice, combinations

def lists_with_product_equal_n(nums):

    def circular_sublists(nums):
        n = len(nums)
        for i in range(n):
            yield (nums[i:] + nums[:i])

    def sublist_has_product_n(sublist, n):
        return n > 0 and (len(sublist) == 1 and sublist[0] == n or (sublist[0] != 0 and sublist_has_product_n(sublist[1:], n // sublist[0])))
    return [sublist for sublist in combinations(circular_sublists(nums), n // 10) if sublist_has_product_n(list(sublist), 10)]