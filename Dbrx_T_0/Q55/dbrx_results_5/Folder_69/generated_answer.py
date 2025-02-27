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
    result = []
    for num in numbers:
        if num == 0 or num == 1:
            continue
        sublists = sublists_with_product_equal_n(numbers, num)
        for sublist in sublists:
            circular_sublists = [list(islice(cycle(sublist), i, i + len(sublist))) for i in range(len(sublist))]
            result.extend(circular_sublists)
    return result