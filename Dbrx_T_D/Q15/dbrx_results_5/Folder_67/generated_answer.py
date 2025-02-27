def sum_odd_ints_inclusive(numbers):
    odd_ints = []
    for num in numbers[22:51]:
        if num % 2 != 0:
            odd_ints.append(num)
    if odd_ints:
        return sum(odd_ints)
    else:
        return 0