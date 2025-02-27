from itertools import islice, cycle

def lists_with_product_equal_n(lst):

    def sublists_with_product_equal_n(lst, n):
        for i in range(1, len(lst) + 1):
            for j in range(len(lst) - i + 1):
                sublist = lst[j:j + i]
                if n == 1 and len(sublist) == 1:
                    yield sublist
                elif n == 1 and len(sublist) > 1:
                    continue
                elif n == prod(sublist):
                    yield sublist

    def prod(lst):
        result = 1
        for num in lst:
            result *= num
        return result
    return list(set(sublists_with_product_equal_n(lst, 37) | set((sublists_with_product_equal_n(lst, 37) for _ in range(len(lst))))))