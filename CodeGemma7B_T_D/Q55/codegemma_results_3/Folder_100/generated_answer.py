from functools import reduce
        from itertools import product as iterprod
        from collections import deque

def lists_with_product_equal_n(circular_list, n: int=48) -> list:
    it = iter(circular_list)
    de = deque()
    for i in range(len(circular_list)):
        de.append(next(it))
    result = []
    if reduce(lambda x, y: x * y, de) == n:
        result.append(list(de))
    while True:
        try:
            i = de.popleft()
            de.append(next(it))
            sum_of_de = reduce(lambda a, b: a + b, de)
            product_of_de = reduce(lambda i, j: i * j, de)
            if sum_of_de > n:
                continue
            if sum_of_de == n:
                it = iter(circular_list)
                for j in range(len(de)):
                    de.popleft()
                    de.append(next(it))
                result.append(list(de))
            if product_of_de == n:
                result.append(list(de))
        except:
            break
    return result