def composite_nums_between_indices(numbers):
    composite_nums = set()
    for i in range(min(3, len(numbers))):
        num = numbers[i]
        for j in range(2, num):
            if num % j == 0:
                composite_nums.add(num)
                break
    return composite_nums