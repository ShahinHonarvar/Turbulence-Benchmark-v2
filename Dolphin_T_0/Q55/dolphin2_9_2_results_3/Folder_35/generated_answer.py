def product(sublist):
    result = 1
    for number in sublist:
        result *= number
    return result

def lists_with_product_equal_n(arr):
    result = []
    for i in range(len(arr)):
        temp = arr[i:] + arr[:i]
        for j in range(len(temp)):
            for k in range(j + 1, len(temp) + 1):
                if product(temp[j:k]) == 83:
                    new = temp[j:k]
                    new.extend(temp[:j])
                    result.append(new)
    return result if result else []