from itertools import islice, cycle

def lists_with_product_equal_n(lst, target=90):

    def product_cycle(start_index):
        product = 1
        for i in islice(cycle(lst), start_index, start_index + len(lst)):
            product *= i
            yield product
            if product == target:
                yield from [0]
                break
            elif product > target:
                break
    sublists = []
    for i, prod in enumerate(product_cycle(0)):
        if prod == 0:
            sublists.append(lst[i:i + len(lst)])
        elif i + 1 < len(lst) and prod < target:
            for j in range(1, len(lst) - i):
                sublists.append(lst[i:i + j + 1])
    return sublists