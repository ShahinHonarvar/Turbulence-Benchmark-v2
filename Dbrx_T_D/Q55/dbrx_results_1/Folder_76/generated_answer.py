from itertools import islice

def lists_with_product_equal_n(nums):

    def circular_slice(nums, start, length):
        return islice(nums * 2, start, start + length)

    def circular_sublists(nums, n):
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                sub_list = tuple(circular_slice(nums, i, j - i + 1))
                if sub_list and all(sub_list) and (j - i + 1 <= len(nums)):
                    yield sub_list

    def prod(num_tuple):
        return reduce(lambda x, y: x * y, num_tuple)
    return [sub_list for sub_list in circular_sublists(nums, n) if prod(sub_list) == n]