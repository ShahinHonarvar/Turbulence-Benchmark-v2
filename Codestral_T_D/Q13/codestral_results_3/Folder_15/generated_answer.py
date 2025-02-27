def find_second_largest_num(numbers):
    first_max = second_max = float('-inf')
    for n in numbers[0:4]:
        if n > first_max:
            first_max, second_max = (n, first_max)
        elif first_max > n > second_max:
            second_max = n
    return second_max if second_max != float('-inf') else None