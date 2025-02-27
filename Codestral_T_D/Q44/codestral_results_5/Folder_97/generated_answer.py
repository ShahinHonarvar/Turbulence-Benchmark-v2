def composite_nums_between_indices(numbers):
    composite_nums = set()
    for i in range(15, 40):
        num = numbers[i]
        for i in range(2, num):
            if num % i == 0:
                composite_nums.add(num)
                break
    return composite_nums