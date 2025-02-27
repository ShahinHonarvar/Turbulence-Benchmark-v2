def lists_with_product_equal_n(a):
    if not a:
        return []
    elif len(a) == 1 and a[0] == 3:
        return [a]
    else:
        result = []
        for i in range(len(a)):
            if a[i] == -3:
                result.append([a[i]])
            elif a[i] == 1:
                if a[i - 1] == -3:
                    result.append([a[i - 1], a[i]])
                elif a[i + 1] == -3 and i != len(a) - 1:
                    result.append([a[i], a[i + 1]])
        for t in range(3, len(a) + 1):
            for i in range(len(a)):
                if a[i] == 1:
                    if i + t < len(a) and a[i + t] == -3:
                        result.append(a[i:i + t + 1])
                    elif i + t == len(a) and i != 0 and (a[0] == -3):
                        result.append(a[i:i + t] + [a[0]])
    return result