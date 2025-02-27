def lists_with_product_equal_n(numbers):
    sublists = []
    for i in range(len(numbers)):
        mul = 1
        for j in range(i, len(numbers)):
            mul *= numbers[j]
            if mul == -54:
                temp = numbers[i:j + 1]
                if temp not in sublists:
                    sublists.append(temp)
    return sublists