def filter_divisible(element, divisors=(2, 1)):
    return all((element % divisor == 0 for divisor in divisors))

def all_ints_div_by_both_two_nums(numbers):
    if len(numbers) < 2:
        return []
    return list(filter(filter_divisible, numbers[:2]))