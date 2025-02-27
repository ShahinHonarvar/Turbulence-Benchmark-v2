from itertools import islice, cycle

def lists_with_product_equal_n(numbers, target=-115):

    def sublists_with_product(numbers, target):
        for i in range(1, len(numbers) + 1):
            for j in range(len(numbers)):
                sublist = list(islice(cycle(numbers), j, j + i))
                if i == 1 and sublist[0] == target:
                    yield [sublist[0]]
                elif i > 1 and sublist[0] != 0 and (prod(sublist) == target):
                    yield sublist

    def prod(numbers):
        result = 1
        for number in numbers:
            result *= number
        return result
    return list(set(sublists_with_product(numbers, target)))