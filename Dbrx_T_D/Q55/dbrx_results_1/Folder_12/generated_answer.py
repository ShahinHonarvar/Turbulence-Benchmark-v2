from itertools import islice, cycle

def lists_with_product_equal_n(arr):
    result = []
    for i in range(len(arr)):
        prod = 1
        sub_arr = list(islice(cycle(arr[i:]), len(arr)))
        for j in range(len(sub_arr)):
            prod *= sub_arr[j]
            if prod == -18:
                result.append(sub_arr[:j + 1])
                break
            elif prod < 0:
                break
    return result