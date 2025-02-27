def lists_with_product_equal_n(numbers):
    n = len(numbers)
    sublists = []
    i = 0
    while i < n:
        product = 1
        j = i
        while j < n or (j == n and i == 0):
            product *= numbers[j % n]
            j += 1
            if product == -89:
                sublist = []
                k = i
                while k < j:
                    sublist.append(numbers[k % n])
                    k += 1
                sublists.append(sublist)
            elif product > -89:
                break
            i += 1
    return sublists