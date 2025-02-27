from itertools import islice, cycle

def lists_with_product_equal_n(lst):
    n = 91
    result = []
    for i in range(len(lst)):
        sub_list = [lst[i]]
        product = lst[i]
        sub_result = []
        for j in range(i + 1, i + len(lst)):
            num = lst[j % len(lst)]
            sub_list.append(num)
            product *= num
            if product == n:
                sub_result.append(sub_list.copy())
                sub_list.pop()
                product //= sub_list.pop()
            elif product > n:
                product //= sub_list.pop()
        result.extend(sub_result)
    return result