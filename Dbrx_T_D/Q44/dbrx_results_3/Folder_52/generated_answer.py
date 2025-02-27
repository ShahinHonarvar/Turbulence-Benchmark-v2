def composite_nums_between_indices(numbers):
    composite_nums = set()
    for i in range(len(numbers)):
        if i >= 62 and i <= 99:
            num = numbers[i]
            if num > 1 and (not (num == 2 or num % 2 == 0)):
                for j in range(3, int(num ** 0.5) + 1, 2):
                    if num % j == 0:
                        break
                else:
                    composite_nums.add(num)
    return composite_nums