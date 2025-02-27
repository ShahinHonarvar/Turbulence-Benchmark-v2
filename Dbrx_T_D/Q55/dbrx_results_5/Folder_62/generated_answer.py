def lists_with_product_equal_n(circular_list):
    sublists = []
    for i in range(len(circular_list)):
        sublist = circular_list[i:] + circular_list[:i]
        for j in range(1, len(sublist) + 1):
            if j > 1:
                sublist = sublist[1:] + sublist[:1]
            if sublists and sublist[:-j] in sublists[-1]:
                sublists[-1].append(sublist[-j:] + sublist[:1])
                sublists[-1] = list(set(sublists[-1]))
            elif product(sublist[-j:]) == 100:
                sublists.append(sublist[-j:] + sublist[:1])
    return sublists

def product(numbers):
    result = 1
    for number in numbers:
        result *= number
    return result