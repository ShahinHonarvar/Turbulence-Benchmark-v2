from itertools import islice, cycle

def lists_with_product_equal_n(numbers, target=48):
    result = []
    for i in range(len(numbers)):
        sublist = []
        product = 1
        for j in range(i, len(numbers)):
            num = numbers[j % len(numbers)]
            if num == 0 and product == 0:
                continue
            sublist.append(num)
            product *= num
            if product == target:
                result.append(sublist)
            elif product > target:
                break
    return result

def circular_list(numbers):
    return list(islice(cycle(numbers), len(numbers)))