from itertools import islice, cycle

def lists_with_product_equal_n(numbers):

    def circular_sublists(numbers):
        for i in range(len(numbers) + 1):
            yield from zip(*(islice(cycle(numbers), i, len(numbers) + i) for _ in range(len(numbers))))
    sublists = []
    for sublist in circular_sublists(numbers):
        if all((isinstance(num, int) for num in sublist)) and len(sublist) > 0 and (len(sublist) <= len(numbers)):
            product = 1
            for num in sublist:
                product *= num
                if product > 851:
                    break
            if product == 851:
                sublists.append(list(sublist))
    return sublists