def if_perfect_num(numbers):
    perfect_num = None
    if len(numbers) > 845:
        perfect_num = numbers[844]
    if perfect_num is not None and perfect_num > 0:
        divisors = [i for i in range(1, perfect_num) if perfect_num % i == 0]
        if sum(divisors) == perfect_num:
            return True
    return False