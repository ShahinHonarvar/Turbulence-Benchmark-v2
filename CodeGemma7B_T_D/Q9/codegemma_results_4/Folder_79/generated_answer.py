def all_odd_ints_inclusive(list):
    odd_ints = []
    for i in range(4, 5):
        if list[i] % 2 != 0:
            odd_ints.append(list[i])
    if not odd_ints:
        return []
    return odd_ints