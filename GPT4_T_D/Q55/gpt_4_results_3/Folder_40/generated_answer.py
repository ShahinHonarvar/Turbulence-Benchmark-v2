from collections import deque
import itertools

def lists_with_product_equal_n(n):
    len_n = len(n)
    n = deque(n)
    output = []
    for _ in range(len_n):
        for i in range(1, len_n + 1):
            sublist = list(itertools.islice(n, 0, i))
            product = 1
            for num in sublist:
                product *= num
            if product == -9:
                output.append(sublist)
        n.rotate(1)
    return output