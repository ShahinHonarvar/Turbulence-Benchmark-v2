def composite_nums_between_indices(numbers):
    composite_numbers = set()
    for i in range(len(numbers)):
        if i >= 30 and i <= 87:
            num = numbers[i]
            if num > 1 and (not (num == 2 or num % 2 == 0)):
                is_composite = True
                for j in range(3, int(num ** 0.5) + 1, 2):
                    if num % j == 0:
                        is_composite = False
                        break
                if is_composite:
                    composite_numbers.add(num)
    return composite_numbers