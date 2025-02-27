from itertools import islice, cycle

def lists_with_product_equal_n(lst):
    n = 46
    result = []
    for i in range(len(lst)):
        window = list(islice(cycle(lst[i:]), len(lst)))
        for j in range(len(window)):
            if j + 1 > i + 1 and j + 1 < len(window):
                current_list = window[j - (i + 1):j + 1]
                if all((num > 0 for num in current_list)) and n % prod(current_list) == 0 and (n // prod(current_list) in current_list):
                    result.append(current_list)
                current_list = window[j - i:j + 1]
                if all((num > 0 for num in current_list)) and n % prod(current_list) == 0 and (n // prod(current_list) in current_list):
                    result.append(current_list)
    return result