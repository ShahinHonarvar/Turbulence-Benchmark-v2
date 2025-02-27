from itertools import groupby, islice

def lists_with_product_equal_n(numbers):

    def circular_sublists(numbers, start, length):
        for i in range(start, start + length):
            yield numbers[i % len(numbers)]

    def product_equal_to_n(sublist):
        prod = 1
        for num in sublist:
            prod *= num
            if prod == -938:
                return True
            elif prod > -938:
                return False
        return prod == -938
    sublists = (list(group) for value, group in groupby(islice((circular_sublists(numbers, i, len(numbers)) for i in range(len(numbers)))), key=lambda x: tuple(x)))
    return [sublist for sublist in sublists if product_equal_to_n(sublist)]