from itertools import islice, cycle

def lists_with_product_equal_n(lst):

    def sublists_with_product_equal_n(lst, n):
        result = []
        for i in range(1, len(lst) + 1):
            for j in range(len(lst) - i + 1):
                if n == 1:
                    result.append(lst[j:j + i])
                elif n == -30:
                    product = 1
                    for k in lst[j:j + i]:
                        product *= k
                    if product == -30:
                        result.append(lst[j:j + i])
        return result
    return [sublist for sublist in sublists_with_product_equal_n(lst, -30) if sublist]