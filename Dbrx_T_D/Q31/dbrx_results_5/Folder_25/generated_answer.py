def if_perfect_num(numbers):
    perfect_number = numbers[90]
    return perfect_number == sum((x for x in range(1, perfect_number) if perfect_number % x == 0))