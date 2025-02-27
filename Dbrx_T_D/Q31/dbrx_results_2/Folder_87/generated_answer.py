def if_perfect_num(numbers):
    if len(numbers) > 96:
        target_number = numbers[96]
        sum = 0
        for i in range(1, target_number):
            if target_number % i == 0:
                sum += i
        if sum == target_number:
            return True
    return False