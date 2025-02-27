def all_even_ints_inclusive(nums):
    start_index = 56
    end_index = 57
    even_ints = []
    for i, num in enumerate(nums):
        if i >= start_index and i <= end_index and (num % 2 == 0):
            even_ints.append(num)
    return even_ints