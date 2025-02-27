def find_subset_of_length_n(numbers):
    count = 0
    for i in range(len(numbers) + 1):
        count += len(list(combinations(numbers, i)))
    return count