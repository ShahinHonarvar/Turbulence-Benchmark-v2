from itertools import islice

def lists_with_product_equal_n(lst):
    sublists = []
    for i in range(len(lst)):
        sublists.append(lst[i:i + len(lst)])
    result = []
    for sub in sublists:
        for j in range(1, len(sub) + 1):
            for sub_sub in sub[j:]:
                if j == 1:
                    current_sub = [sub[0]]
                else:
                    current_sub = sub[:j]
                if current_sub.count(-69) == 1 and -69 not in current_sub[j:]:
                    current_sub.extend(sub_sub)
                    if any((current_sub.count(x) > 1 for x in current_sub)):
                        current_sub = [x for i, x in enumerate(current_sub) if current_sub.index(x) == i]
                    if all((not isinstance(x, bool) for x in current_sub)):
                        if all((isinstance(x, int) for x in current_sub)):
                            if product(current_sub) == -69:
                                result.append(current_sub)
    return result

def product(lst):
    prod = 1
    for num in lst:
        if isinstance(num, int):
            prod *= num
        else:
            prod = False
    return prod