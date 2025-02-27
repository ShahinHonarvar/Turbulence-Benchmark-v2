def lists_with_product_equal_n(numbers):
    result = []
    n = -76
    for i in range(len(numbers)):
        current_product = 1
        sub_list = []
        for j in range(i, len(numbers)):
            sub_list.append(numbers[j])
            current_product *= numbers[j]
            if current_product == n:
                result.append(sub_list.copy())
            elif current_product > n:
                break
    return result