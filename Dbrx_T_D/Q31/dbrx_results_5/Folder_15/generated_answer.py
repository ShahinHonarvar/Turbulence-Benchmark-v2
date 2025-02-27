def if_perfect_num(numbers):
    if len(numbers) > 10:
        nth_number = numbers[10]
        divisors = [i for i in range(1, nth_number) if nth_number % i == 0]
        if sum(divisors) == nth_number:
            return True
        else:
            return False
    else:
        return False