def composite_nums_between_indices(numbers):
    composite_nums = set()
    for num in numbers[60:201]:
        for i in range(2, num):
            if num % i == 0:
                composite_nums.add(num)
                break
    return composite_nums