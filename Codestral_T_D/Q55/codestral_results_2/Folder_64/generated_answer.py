from itertools import cycle, islice

def lists_with_product_equal_n(lst):
    n = 3
    result = []
    for i in range(len(lst)):
        if lst[i] == n:
            result.append([lst[i]])
        else:
            product = lst[i]
            temp = [lst[i]]
            for j in islice(cycle(lst), i + 1, len(lst)):
                product *= lst[j]
                temp.append(lst[j])
                if product == n:
                    result.append(temp)
                elif product > n:
                    break
    return result