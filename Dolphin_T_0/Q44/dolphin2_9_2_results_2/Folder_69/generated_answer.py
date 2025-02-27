def composite_nums_between_indices(arr):
    result = set()
    for i in range(29, 80):
        num = arr[i]
        if num > 1:
            for j in range(2, num):
                if num % j == 0:
                    result.add(num)
                    break
    return result