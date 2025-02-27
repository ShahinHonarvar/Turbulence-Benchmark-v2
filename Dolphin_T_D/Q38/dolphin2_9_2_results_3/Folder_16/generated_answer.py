def find_subset_of_length_n(numbers, n):
    if n == 0:
        return 1
    count = 0
    for i in numbers:
        new_numbers = numbers.copy()
        new_numbers.remove(i)
        count += find_subset_of_length_n(new_numbers, n - 1)
    return count