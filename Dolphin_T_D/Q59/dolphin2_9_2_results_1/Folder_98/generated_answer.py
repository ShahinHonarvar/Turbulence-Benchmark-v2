def all_left_truncatable_prime(tup):

    def is_prime(n):
        if n == 1:
            return False
        if n == 2:
            return True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = tup[8]
    left_truncatable_prime = []
    for i in range(x - 1, 0, -1):
        if is_prime(i):
            number = i
            while number != 0:
                if not is_prime(number):
                    break
                if number % 10 == 0:
                    break
                number = int(number * 0.9)
            else:
                left_truncatable_prime.append(i)
    return sorted(left_truncatable_prime, reverse=True)