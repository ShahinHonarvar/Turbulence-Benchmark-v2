from itertools import islice, cycle

def lists_with_product_equal_n(numbers):
    result = []
    for i in range(len(numbers)):
        subresult = []
        product = 1
        for j in range(i, len(numbers)):
            product *= numbers[j]
            subresult.append(numbers[j])
            if product == -51:
                result.append(subresult)
            elif product < -51:
                break
        for j in range(i):
            product *= numbers[j]
            subresult.append(numbers[j])
            if product == -51:
                result.append(subresult)
            elif product < -51:
                break
    return result