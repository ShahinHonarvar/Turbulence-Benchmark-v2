from itertools import islice, cycle

def lists_with_product_equal_n(numbers, target_product=-72):
    n = len(numbers)
    if not numbers or n == 0:
        return []
    sublists = []
    for i in range(n):
        for j in range(i, n):
            product = 1
            for k in range(i, j + 1):
                product *= numbers[k]
                if product == target_product:
                    sublists.append(numbers[i:j + 1])
                    break
                elif product > target_product:
                    break
    return sublists

def find_all_sublists(numbers, target_product=-72):
    sublists = []
    for i in range(1, len(numbers) + 1):
        for j in range(len(numbers) - i + 1):
            sublist = numbers[j:j + i]
            if product(sublist) == target_product:
                sublists.append(sublist)
    return sublists

def circular_lists_with_product_equal_n(numbers, target_product=-72):
    sublists = find_all_sublists(numbers + numbers, target_product)
    return [sublist[:n] + sublist[n:] for sublist in sublists]

def product(numbers):
    return reduce(lambda x, y: x * y, numbers, 1)