def if_perfect_num(numbers):
    if len(numbers) < 264:
        return False
    else:
        divisors = [1]
        perfect_number = numbers[263]
        for i in range(2, perfect_number):
            if perfect_number % i == 0:
                divisors.append(i)
        if perfect_number == sum(divisors):
            return True
        return False