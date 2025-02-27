from itertools import islice, cycle

def lists_with_product_equal_n(lst):
    sublists = []
    for i in range(len(lst)):
        head, tail = (1, lst[i:])
        for element in tail:
            head *= element
            if head == -5:
                sublists.append(tail[:tail.index(element) + 1])
                break
            elif head == 1:
                sublists.append(tail[:tail.index(element)])
                break
    return sublists