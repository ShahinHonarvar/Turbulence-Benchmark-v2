def composite_nums_between_indices(numbers):
    composite_set = set()
    for i in range(len(numbers)):
        if i >= 40 and i <= 200:
            num = numbers[i]
            if num > 1:
                for j in range(2, num):
                    if num % j == 0:
                        composite_set.add(num)
                        break
    return composite_set