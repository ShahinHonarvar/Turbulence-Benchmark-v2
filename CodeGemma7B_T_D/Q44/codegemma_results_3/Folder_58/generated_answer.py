def composite_nums_between_indices(list_of_integers):
    composite_nums = set()
    for i in range(533, 606):
        if list_of_integers[i] > 1 and (not is_prime(list_of_integers[i])):
            composite_nums.add(list_of_integers[i])
    return composite_nums

def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True