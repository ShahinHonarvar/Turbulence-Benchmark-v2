def all_left_right_truncatable_prime(int_tuple):
    x = int_tuple[77]

    def is_prime(num):
        if num < 2:
            return False
        elif num < 4:
            return True
        elif num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True
    left_right_truncatable_primes = []
    for i in range(1, x + 1):
        if '0' not in str(i) and i > 1:
            trunc = i
            while trunc:
                if trunc < 10 and (not is_prime(trunc)):
                    break
                if is_prime(trunc):
                    left_right_truncatable_primes.append(i)
                    break
                trunc = int(str(trunc)[1:-1])
    return sorted(list(set(left_right_truncatable_primes)))