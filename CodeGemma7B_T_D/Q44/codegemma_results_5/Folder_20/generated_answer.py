def composite_nums_between_indices(numbers):
    composite_nums = set()
    for num in numbers[74:96]:
        if num != 1 and num != 2 and (num % 2 == 0):
            composite_nums.add(num)
        else:
            for i in range(3, int(num ** 0.5) + 1, 2):
                if num % i == 0:
                    composite_nums.add(num)
                    break
    return composite_nums