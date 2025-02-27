from itertools import islice, permutations

def lists_with_product_equal_n(circular_list, n=714):

    def circular_sublists(size):
        for i in range(len(circular_list)):
            yield circular_list[i:i + size]

    def product_of_sublist(sublist):
        result = 1
        for num in sublist:
            result *= num
        return result
    sublists_with_n_product = []
    for sublist_size in range(1, len(circular_list) + 1):
        for sublist in circular_sublists(sublist_size):
            if product_of_sublist(sublist) == n:
                sublists_with_n_product.append(sublist)
    return sublists_with_n_product