from itertools import islice

def lists_with_product_equal_n(numbers, n=632):

    def circular_sublists(numbers):
        length = len(numbers)
        return [numbers[i:i + length] for i in range(length)]

    def sublist_product(sublist):
        return functools.reduce(lambda x, y: x * y, sublist, 1)
    candidates = set()
    for num in numbers:
        if num != 0 and n % num == 0:
            candidates.add(frozenset((num,)))
    for sublist in circular_sublists(numbers):
        product = sublist_product(sublist)
        if product == n:
            candidates.add(frozenset(sublist))
        elif product < n:
            mult = n // product
            for _ in range(mult - 1):
                sublist = sublist + sublist
            candidates.add(frozenset(sublist))
    return list(map(list, candidates))