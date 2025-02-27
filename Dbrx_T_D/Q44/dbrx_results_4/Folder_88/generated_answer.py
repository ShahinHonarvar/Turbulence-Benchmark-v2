def composite_nums_between_indices(numbers):
    if len(numbers) < 10:
        return set()
    composite_numbers = set()
    for i in range(8, 10):
        num = numbers[i]
        if num > 1 and (not (num % 2 == 0 and num > 2)):
            if num % 2 == 0 or num % 3 == 0 or (num % 5 == 0 and num > 5):
                composite_numbers.add(num)
            else:
                found_prime = False
                for j in range(7, int(num ** 0.5) + 1, 6):
                    if num % j == 0 or num % (j + 2) == 0:
                        found_prime = True
                        break
                if not found_prime:
                    composite_numbers.add(num)
    return composite_numbers