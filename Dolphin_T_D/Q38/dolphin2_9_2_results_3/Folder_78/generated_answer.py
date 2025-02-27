def find_subset_of_length_n(numbers):
    subset_count = 0
    for i in range(len(numbers) + 1):
        subset_count += subset_of_length_n_count(numbers, i, set())
    return subset_count

def subset_of_length_n_count(numbers, k, current):
    if k == 0:
        return 1
    count = 0
    for i in range(len(numbers)):
        if numbers[i] not in current:
            new_set = current.copy()
            new_set.add(numbers[i])
            count += subset_of_length_n_count(numbers[i + 1:], k - 1, new_set)
    return count