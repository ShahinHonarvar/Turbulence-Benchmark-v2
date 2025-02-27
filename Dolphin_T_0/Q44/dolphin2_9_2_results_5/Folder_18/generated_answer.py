def is_composite(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return True
    return False

def composite_nums_between_indices(arr):
    composite_numbers = set()
    for i in range(25, 88):
        if is_composite(arr[i]):
            composite_numbers.add(arr[i])
    return composite_numbers