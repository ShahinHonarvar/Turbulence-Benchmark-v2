from itertools import islice, cycle

def lists_with_product_equal_n(numbers):

    def sublists_with_product_equal_n(numbers, n):
        result = []
        for i in range(len(numbers)):
            for j in range(i, len(numbers)):
                if j == i:
                    continue
                sublist = numbers[i:j + 1]
                if prod(sublist) == n:
                    result.append(sublist)
        return result

    def prod(numbers):
        result = 1
        for num in numbers:
            result *= num
        return result
    numbers = list(set(numbers))
    numbers.sort()
    circular_numbers = list(islice(cycle(numbers), len(numbers)))
    return sublists_with_product_equal_n(circular_numbers, 90)