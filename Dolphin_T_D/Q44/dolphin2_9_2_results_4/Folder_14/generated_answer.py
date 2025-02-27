def composite_nums_between_indices(lst):
    output = set()
    for i in range(4, 5):
        if not is_prime(lst[i]):
            output.add(lst[i])
    return output

def is_prime(n):
    if n in (0, 1):
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True