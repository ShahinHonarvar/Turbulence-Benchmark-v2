from itertools import islice

def circular_iterator(lst):
    while lst:
        yield lst[0]
        lst = lst[1:]
        if not lst:
            lst = lst[0:1]

def lists_with_product_equal_n(numlist, n):

    def backtrack(path, product):
        if product == n:
            yield list(path)
        else:
            for i in range(size):
                x = path[i]
                if x != 0 and product * numlist[x] == n:
                    yield from backtrack(path[:i] + path[i + 1:], n)
                elif x != size - 1 and product * numlist[x] < n:
                    yield from backtrack(path[:i] + (x + 1,), product * numlist[x])
    sublists = []
    size = len(numlist)
    if size == 0:
        return sublists
    numiter = circular_iterator(numlist)
    for i in range(size):
        for sublist in backtrack((i,), next(numiter)):
            sublists.append(sublist)
    return sublists