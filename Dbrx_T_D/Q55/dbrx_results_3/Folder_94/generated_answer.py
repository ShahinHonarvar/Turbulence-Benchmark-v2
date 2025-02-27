from itertools import islice, cycle

def lists_with_product_equal_n(numbers, target=-30):
    result = []
    for i in range(len(numbers)):
        sublist = list(islice(cycle(numbers[i:] + numbers[:i]), len(numbers)))
        for j in range(len(sublist)):
            product = 1
            for k in sublist[j:j + 3]:
                product *= k
            if product == target:
                result.append(sublist[j:j + 3])
    return result