from itertools import islice, cycle

def lists_with_product_equal_n(circular_list):

    def sublists_with_product_equal_n(lst, n=3):
        result = []
        for i in range(len(lst)):
            for j in range(len(lst)):
                if lst[i:j + 1] and functools.reduce(lambda x, y: x * y, lst[i:j + 1]) == n:
                    result.append(lst[i:j + 1])
        return result
    circular_list = list(circular_list)
    circular_list = circular_list + circular_list[:1]
    return [sublist for sublist in sublists_with_product_equal_n(circular_list) if sublist not in [sublist2 for sublist2 in sublists_with_product_equal_n(circular_list, n) if sublist2 == sublist and sublist2[0] < sublist[0]]]