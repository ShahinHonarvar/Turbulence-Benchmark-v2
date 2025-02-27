def if_perfect_num(numbers):
    if len(numbers) > 96:
        target_number = numbers[96]
        sum_divisors = 0
        for i in range(1, target_number):
            if target_number % i == 0:
                sum_divisors += i
        if sum_divisors == target_number:
            return True
        else:
            return False
    else:
        return False