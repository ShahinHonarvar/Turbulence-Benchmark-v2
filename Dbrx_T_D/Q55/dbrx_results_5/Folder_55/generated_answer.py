from itertools import permutations

def circular_list_product(numbers, head_index=0):
    head = numbers[head_index]
    tail = numbers[(head_index + 1) % len(numbers)]
    product = head * tail
    if len(numbers) == 2:
        return product
    else:
        return product * circular_list_product(numbers[1:] + numbers[:1], (head_index + 1) % len(numbers))

def lists_with_product_equal_n(numbers, target):
    result = []
    for i in range(len(numbers)):
        subnumbers = numbers[i:] + numbers[:i]
        if circular_list_product(subnumbers) == target:
            result.append(subnumbers)
    return result