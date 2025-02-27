def prime_factors(lst):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    lst_num = lst[8]
    result_set = set()
    for i in range(2, lst_num + 1):
        if is_prime(i) and lst_num % i == 0:
            result_set.add(i)
    return result_set