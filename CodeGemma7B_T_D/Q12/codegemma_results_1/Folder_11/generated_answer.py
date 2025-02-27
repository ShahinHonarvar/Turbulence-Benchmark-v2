def find_smallest_num(numbers):
    small = numbers[25]
    for num in numbers[25:60]:
        if num < small:
            small = num
    return small