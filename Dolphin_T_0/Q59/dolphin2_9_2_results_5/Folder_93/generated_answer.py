def all_left_truncatable_prime(positive_integers):

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
    x = positive_integers[11]
    return sorted([i for i in range(2, x) if is_prime(i) and (not any((val % 10 ** j == 0 or not is_prime(val // 10 ** j) for j in range(1, len(str(i))))))])