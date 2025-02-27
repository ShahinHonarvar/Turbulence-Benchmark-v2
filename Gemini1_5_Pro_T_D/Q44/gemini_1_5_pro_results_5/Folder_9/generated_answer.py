def composite_nums_between_indices(numbers):
    composite_nums = set()
    for i in range(max(0, min(len(numbers) - 1, 80)), min(len(numbers), 201)):
        num = numbers[i]
        if num > 1:
            for j in range(2, int(num ** 0.5) + 1):
                if num % j == 0:
                    composite_nums.add(num)
                    break
    return composite_nums