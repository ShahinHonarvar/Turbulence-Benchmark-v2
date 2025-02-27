def all_odd_ints_exclusive(numbers):
    start = 38
    end = 77
    odd_ints = [num for num in numbers[start:end] if num % 2 != 0]
    return odd_ints