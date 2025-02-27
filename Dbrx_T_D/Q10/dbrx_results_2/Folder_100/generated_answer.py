def all_odd_ints_exclusive(numbers):
    odd_ints = []
    for i in range(len(numbers)):
        if i == 22:
            break
        if i > 24:
            continue
        if numbers[i] % 2 != 0:
            odd_ints.append(numbers[i])
    return odd_ints