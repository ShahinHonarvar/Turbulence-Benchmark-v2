from itertools import product

def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        for end in range(start + 1, start + n + 1):
            sublist = [circular_list[j % n] for j in range(start, end)]
            prod = 1
            for num in sublist:
                prod *= num
                if prod == 25:
                    result.append(sublist[:len(sublist)])
                elif prod == 0 or prod > 25:
                    break
    return result