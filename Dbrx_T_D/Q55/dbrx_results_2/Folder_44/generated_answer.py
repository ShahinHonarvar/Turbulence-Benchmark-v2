from itertools import islice, cycle

def lists_with_product_equal_n(lst, n=29):

    def sublists_with_product(lst):
        result = []
        for size in range(1, len(lst) + 1):
            for i in range(len(lst) - size + 1):
                sublist = lst[i:i + size]
                if size != 1 or lst[i] != 1:
                    product = 1
                    for num in sublist:
                        product *= num
                    if product == n:
                        result.append(sublist)
        return result
    circular_lst = list(islice(cycle(lst), len(lst) * 2 - 1, len(lst) * 2 + len(lst) - 1))
    return sublists_with_product(circular_lst)