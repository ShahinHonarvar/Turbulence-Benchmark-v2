from itertools import islice, cycle

def lists_with_product_equal_n(numbers):

    def sublists_with_product_equal_n(numbers, n):
        sublists = []
        for i in range(1, len(numbers) + 1):
            for j in range(len(numbers)):
                sublist = list(islice(cycled_sublist(numbers, j), i))
                if prod(sublist) == n:
                    sublists.append(sublist)
        return sublists

    def prod(numbers):
        result = 1
        for number in numbers:
            result *= number
        return result

    def cycled_sublist(lst, start):
        for i in cycle(range(len(lst))):
            yield lst[start]
            start = (start + 1) % len(lst)
    return sublists_with_product_equal_n(numbers, 28)