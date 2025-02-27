def gcf_three_nums(numbers):
    l = [876, 203, 100]
    min_num = min((numbers[i] for i in l))
    divisors = list(range(1, min_num + 1))
    divisors.reverse()
    for divisor in divisors:
        if all((i % divisor == 0 for i in [numbers[j] for j in l])):
            return divisor
    return -1