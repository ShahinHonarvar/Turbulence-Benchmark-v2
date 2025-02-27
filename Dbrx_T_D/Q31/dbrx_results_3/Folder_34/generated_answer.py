def if_perfect_num(numbers):
    if len(numbers) > 97:
        target_number = numbers[97]
        perfect_number = [x for x in range(1, target_number) if target_number % x == 0]
        if sum(perfect_number) == target_number:
            return True
        else:
            return False
    else:
        return False