def if_perfect_num(numbers):
    if len(numbers) > 85 and numbers[85] == get_sum_of_divisors(numbers[85]):
        return True
    else:
        return False

def get_sum_of_divisors(n):
    sum = 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i:
            continue
        if i != n // i:
            sum += i + n // i
        else:
            sum += i
    return sum