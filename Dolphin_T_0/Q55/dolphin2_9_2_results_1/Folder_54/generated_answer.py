def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    if n > 1:
        for i in range(n):
            product = 1
            for j in range(i, n * 2):
                if lst[j % n] == 0:
                    product = 0
                else:
                    product *= lst[j % n]
                if product == -17:
                    temp = []
                    k = j
                    while k > j - n and len(temp) < n:
                        if lst[k % n] != 0:
                            temp.append(lst[k % n])
                        else:
                            temp = []
                            break
                        k -= 1
                    if len(temp) > 0:
                        temp.reverse()
                        result.append(temp)
    return result