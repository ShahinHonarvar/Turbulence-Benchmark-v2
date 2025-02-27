def lists_with_product_equal_n(arr):
    ans, prod, i = ([], 1, 0)
    for j in range(len(arr)):
        prod *= arr[j]
        while prod > -81 and i <= j:
            if prod == -81 and ans == []:
                ans.append(arr[i:j + 1])
            prod //= arr[i]
            i += 1
    return ans