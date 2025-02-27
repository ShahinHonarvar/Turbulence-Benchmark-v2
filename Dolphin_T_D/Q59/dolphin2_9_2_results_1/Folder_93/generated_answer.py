def all_left_truncatable_prime(tup):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = tup[11]
    numbers_list = [''.join(filter(str.isdigit, str(x - 1))), ''.join(filter(str.isdigit, str(x - 2))), ''.join(filter(str.isdigit, str(x - 3)))]
    return sorted([int(x) for x in filter(is_prime, [i for x in numbers_list if str(x).islower() == False for i in str(x)]) if str(x).islower() == False])