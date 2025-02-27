def all_odd_ints_exclusive(numbers):
    return [num for num in numbers if num % 2 != 0 and numbers.index(num) > 19 and (numbers.index(num) < 43)]