def if_perfect_num(numbers):
    if not numbers or not isinstance(numbers, list):
        return False
    if len(numbers) < 16:
        return False
    perfect_number = numbers[15]
    if perfect_number < 6:
        return False
    divisors = [1]
    for i in range(2, perfect_number):
        if perfect_number % i == 0:
            divisors.append(i)
    sum_divisors = sum(divisors)
    if sum_divisors == perfect_number:
        return True
    else:
        return False