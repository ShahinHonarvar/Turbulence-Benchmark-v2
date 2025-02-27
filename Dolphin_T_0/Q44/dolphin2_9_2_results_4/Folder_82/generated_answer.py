def composite_nums_between_indices(lst):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    composite_nums = set()
    for i in range(30, 100000):
        number = lst[i]
        if not is_prime(number):
            composite_nums.add(number)
    return composite_nums