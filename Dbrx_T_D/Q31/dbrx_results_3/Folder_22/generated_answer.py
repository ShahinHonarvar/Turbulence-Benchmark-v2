def if_perfect_num(numbers):
    if len(numbers) > 72 and numbers[72] == get_sum_of_proper_divisors(numbers[72]):
        return True
    else:
        return False

def get_sum_of_proper_divisors(number):
    sum = 1
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            if i == number // i:
                sum += i
            else:
                sum += i + number // i
    return sum