def sum_odd_ints_inclusive(numbers):
    odd_ints = [num for num in numbers[36:77] if num % 2 != 0]
    return sum(odd_ints) if odd_ints else 0