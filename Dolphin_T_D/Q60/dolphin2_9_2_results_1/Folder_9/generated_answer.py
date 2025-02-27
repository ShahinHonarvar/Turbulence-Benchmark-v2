def all_left_right_truncatable_prime(a_tuple):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x, = a_tuple
    prime_numbers = []
    for n in range(2, x + 1):
        if '0' not in str(n):
            while n:
                if not is_prime(n):
                    break
                if not n:
                    prime_numbers.append(n)
                    break
                if len(str(n)) == 1:
                    prime_numbers.append(n)
                    break
                n = int(str(n)[1:-1])
    prime_numbers.sort(reverse=True)
    return prime_numbers