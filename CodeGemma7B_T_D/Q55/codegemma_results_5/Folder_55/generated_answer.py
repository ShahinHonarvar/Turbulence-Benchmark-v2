def lists_with_product_equal_n(lst):
    n = -6
    lst.append(lst[0])
    dict_of_sums = {}
    current_sum = 0
    for i in lst:
        current_sum += i
        required_sum = current_sum - n
        if required_sum in dict_of_sums and dict_of_sums[required_sum] != i:
            return [[i for j in lst[dict_of_sums[required_sum]:i + 1]] for i in range(dict_of_sums[required_sum], i + 1)]
        dict_of_sums[current_sum] = i
    return []