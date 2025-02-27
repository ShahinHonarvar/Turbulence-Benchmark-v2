def lists_with_product_equal_n(lst):

    def contiguous_sublists(lst, start: int=0, product: int=1):
        for i in range(start, len(lst)):
            curr_product = product
            for j in range(i, len(lst)):
                curr_product *= lst[j]
                if curr_product == n:
                    break
            yield [e for e in lst[i:j + 1]]
    n = 78
    return list(set([lst for n in range(1, len(lst)) for lst in contiguous_sublists(lst, i=n, product=1)]))