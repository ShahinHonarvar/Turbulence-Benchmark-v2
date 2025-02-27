def composite_nums_between_indices(arr):
    composite_nums = set()
    for i in range(20, 201):
        num = arr[i]
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    composite_nums.add(num)
                    break
    return composite_nums