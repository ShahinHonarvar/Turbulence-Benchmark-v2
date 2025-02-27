def if_perfect_num(numbers):
    if len(numbers) > 93:
        target_number = numbers[93]
        total = 0
        for i in range(1, target_number):
            if target_number % i == 0:
                total += i
        return total == target_number
    else:
        return False