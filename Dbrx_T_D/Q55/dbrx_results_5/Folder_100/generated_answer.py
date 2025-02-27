from itertools import islice, cycle

def lists_with_product_equal_n(numbers, target=48):
    result = []
    for i in range(len(numbers)):
        sublist = list(islice(cycle(numbers[i:]), len(numbers)))
        for j in range(len(sublist)):
            if (prod := reduce(lambda a, b: a * b, sublist[j:j + 3])) == target:
                result.append(sublist[j:j + 3])
    return result