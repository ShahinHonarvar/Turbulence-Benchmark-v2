def all_right_truncatable_prime(tuple_of_positive_integers):

    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = tuple_of_positive_integers[6]
    all_prime = []
    for i in range(x - 1, 1, -1):
        if is_prime(i):
            temp = i
            while temp > 0:
                if not is_prime(temp):
                    break
                temp //= 10
                if temp == 0:
                    all_prime.append(i)
    return sorted(all_prime, reverse=True)