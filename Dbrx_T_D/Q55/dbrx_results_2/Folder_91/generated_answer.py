from itertools import islice

def circular_list_elements(n):

    def circular_sublists(lst):
        for i in range(len(lst)):
            yield (lst[i:] + lst[:i])

    def lists_with_product_equal_n(n, lst):
        result = []
        for sublist in circular_sublists(lst):
            for i in range(1, len(sublist) + 1):
                if prod(sublist[:i]) == n:
                    result.append(sublist[:i])
        return result

    def prod(lst):
        result = 1
        for i in lst:
            result *= i
        return result
    return lists_with_product_equal_n