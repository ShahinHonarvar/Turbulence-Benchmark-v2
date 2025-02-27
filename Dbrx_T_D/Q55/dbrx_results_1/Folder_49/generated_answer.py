from itertools import islice

def lists_with_product_equal_n(circular_list, n):

    def sublists_with_product_equal_n(sequence, n):
        result = []
        for i in range(len(sequence)):
            for j in range(i, len(sequence)):
                if j == i:
                    current_sublist = [sequence[i]]
                else:
                    current_sublist.append(sequence[j])
                if prod(current_sublist) == n:
                    result.append(current_sublist)
                if prod(current_sublist) > n and j < len(sequence) - 1:
                    break
        return result

    def prod(sequence):
        product = 1
        for num in sequence:
            product *= num
        return product
    if len(circular_list) < 3:
        return sublists_with_product_equal_n(circular_list, n)
    result = []
    for i in range(len(circular_list)):
        if i != len(circular_list) - 1:
            sublist = circular_list[i:]
            sublist.extend(circular_list[:i])
        else:
            sublist = circular_list[i:]
            sublist.extend(circular_list[i + 1:i + 1 + len(circular_list) - n.len()])
        result.extend(sublists_with_product_equal_n(sublist, n))
    return result