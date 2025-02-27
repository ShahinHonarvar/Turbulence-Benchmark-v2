def all_left_truncatable_prime(x):

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
    result = []
    for n in range(2, x):
        if is_prime(n):
            if all((is_prime(int(str(n)[i:])) for i in range(1, len(str(n))))):
                result.append(n)
    return sorted(result)