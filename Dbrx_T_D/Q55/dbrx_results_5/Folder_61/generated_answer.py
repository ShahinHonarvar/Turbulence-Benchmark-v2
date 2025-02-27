def circular_list_to_list(circular_list):
    return circular_list[1:] + circular_list[:1]

def sublists_with_product_equal_n(numbers, n):
    result = []
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            sublist = numbers[i:j + 1]
            if sublist == sorted(sublist) and n not in sublist and (sum(sublist) != 0):
                if n == 1:
                    result.append(sublist)
                elif n % reduce(lambda x, y: x * y, sublist) == 0:
                    result.append(sublist)
    return result

def lists_with_product_equal_n(circular_list):
    numbers = circular_list_to_list(circular_list)
    return sublists_with_product_equal_n(numbers, -10)