from itertools import islice, cycle

def lists_with_product_equal_n(numbers):

    def sublists_with_product_equal_n(numbers, n):
        for i in range(len(numbers)):
            for j in range(i, len(numbers)):
                if j == i:
                    yield [numbers[i]]
                elif prod(numbers[i:j + 1]) == n:
                    yield numbers[i:j + 1]

    def prod(numbers):
        result = 1
        for number in numbers:
            result *= number
        return result
    return [sublist for sublist in sublists_with_product_equal_n(cycle(numbers), -81) if len(sublist) <= len(numbers)]