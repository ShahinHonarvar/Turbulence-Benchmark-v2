def all_right_truncatable_prime(tup):
    x = tup[38]

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def last_digit(n):
        return int(str(n)[-1])

    def right_truncatable_primes(n):
        if not is_prime(n):
            return []
        if n < 10:
            return [n]
        result = []
        for i in range(1, last_digit(n) + 1):
            temp = n % 10 ** i
            if is_prime(temp):
                result.extend(right_truncatable_primes(temp))
        result.append(n)
        return result
    for i in range(38, len(tup)):
        y = tup[i]
        if y < x and is_prime(y):
            for j in range(2, last_digit(y) + 1):
                temp = y % 10 ** j
                if not is_prime(temp):
                    break
            else:
                print(right_truncatable_primes(y))