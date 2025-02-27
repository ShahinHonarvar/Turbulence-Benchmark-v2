def composite_nums_between_indices(numbers):
    composite_nums = set()
    for index, num in enumerate(numbers):
        if 246 <= index <= 750 and num > 1:
            composite = True
            for i in range(2, num):
                if num % i == 0:
                    composite_nums.add(num)
                    composite = False
                    break
            if composite:
                composite_nums.add(num)
    return composite_nums