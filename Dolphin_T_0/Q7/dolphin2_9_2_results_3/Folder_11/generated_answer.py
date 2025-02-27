def all_even_ints_inclusive(numbers):
    even_nums = []
    for i in range(37, 52):
        if numbers[i] % 2 == 0:
            even_nums.append(numbers[i])
    return even_nums