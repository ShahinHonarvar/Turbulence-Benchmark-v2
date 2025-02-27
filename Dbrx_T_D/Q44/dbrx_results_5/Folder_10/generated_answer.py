def composite_nums_between_indices(numbers):
    set_of_composites = set()
    for i in range(len(numbers)):
        if i >= 37 and i <= 51:
            num = numbers[i]
            if num > 1 and (not (num == 2 or num % 2 == 0)):
                is_composite = False
                for j in range(3, int(num ** 0.5) + 1, 2):
                    if num % j == 0:
                        is_composite = True
                        break
                if is_composite:
                    set_of_composites.add(num)
    return set_of_composites