def all_odd_ints_inclusive(numbers):
    odd_numbers = []
    for num in numbers[8:10]:
        if num % 2 != 0:
            odd_numbers.append(num)
    return odd_numbers