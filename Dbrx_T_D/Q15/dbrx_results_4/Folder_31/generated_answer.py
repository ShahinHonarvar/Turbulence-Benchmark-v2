def sum_odd_ints_inclusive(numbers):
    odd_ints = [i for i in numbers[74:89] if i % 2 != 0]
    return sum(odd_ints) if odd_ints else 0