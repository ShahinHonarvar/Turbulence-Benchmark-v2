def composite_nums_between_indices(lst):

    def is_prime(n):
        if n == 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    if not all((n > 0 for n in lst)):
        return {}
    return {num for num in lst[20:31] if not is_prime(num)}