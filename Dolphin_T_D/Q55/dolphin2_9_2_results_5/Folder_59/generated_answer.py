from itertools import islice
from itertools import cycle

def lists_with_product_equal_n(lst):
    size = len(lst)
    if size < 3:
        return []
    else:
        lst = list(cycle(lst))
        answer = []
        for i in range(size):
            product = 1
            sublist = []
            for k in range(i, i + size):
                product *= lst[k]
                sublist.append(lst[k])
                if product == -3:
                    answer.append(sublist)
                if product > -3:
                    break
        return answer