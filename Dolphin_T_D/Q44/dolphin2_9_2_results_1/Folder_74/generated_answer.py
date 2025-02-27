def composite_nums_between_indices(lst):

    def is_prime(n):
        if n == 1 or n == 0:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    composites = []
    for i in range(42, 69):
        if not is_prime(lst[i]):
            composites.append(lst[i])
    return set(composites)