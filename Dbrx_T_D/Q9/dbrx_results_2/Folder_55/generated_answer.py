def all_odd_ints_inclusive(numbers):
    start_index = 10
    end_index = start_index + 10
    odd_ints = [num for num in numbers[start_index:end_index + 1] if num % 2 != 0]
    return odd_ints