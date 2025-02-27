from itertools import islice, cycle

def lists_with_product_equal_n(numbers):
    result = []
    circular_numbers = cycle(numbers)
    circular_products = []
    for i, num in enumerate(circular_numbers):
        circular_products.append(circular_products[-1] * num if i != 0 else num)
    for i in range(len(numbers)):
        subset = list(islice(circular_numbers, i, len(numbers) + i))
        subset_product = 1
        for num in subset:
            subset_product *= num
            if subset_product == 23:
                result.append(subset)
                break
            if subset_product < 0 and subset_product * -1 in circular_products:
                j = circular_products.index(subset_product * -1)
                if j < i:
                    result.append(subset)
                    break
    return result