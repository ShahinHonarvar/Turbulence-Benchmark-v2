def if_perfect_num(numbers):
    if len(numbers) < 16:
        return False
    else:
        perfect_number = numbers[15]
        divisors = [1]
        for i in range(2, perfect_number):
            if perfect_number % i == 0:
                divisors.append(i)
        if sum(divisors) == perfect_number:
            return True
        else:
            return False