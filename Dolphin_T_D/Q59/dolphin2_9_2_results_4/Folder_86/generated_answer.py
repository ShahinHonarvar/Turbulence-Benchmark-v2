def all_left_truncatable_prime(tuple_of_ints):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = tuple_of_ints[126]
    primes = [3, 7]
    for num in range(11, x):
        if is_prime(num):
            str_num = str(num)
            if all((is_prime(int(str_num[i:])) for i in range(len(str_num) - 1))):
                primes.append(num)
    primes.sort(reverse=True)
    return primes