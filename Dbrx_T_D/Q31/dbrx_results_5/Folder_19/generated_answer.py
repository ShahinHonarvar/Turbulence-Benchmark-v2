def if_perfect_num(numbers):
    if len(numbers) > 13:
        perfect_num = numbers[13]
        divisors = [i for i in range(1, perfect_num) if perfect_num % i == 0]
        if sum(divisors) == perfect_num:
            return True
        else:
            return False
    else:
        return False