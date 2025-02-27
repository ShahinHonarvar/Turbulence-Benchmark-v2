def all_left_truncatable_prime(tuples):
    x = tuples[18]

    def is_left_truncatable_prime(n):
        if str(n).count('0') == 0:
            m = n
            while m > 0:
                if all((m % i != 0 for i in range(2, int(m ** 0.5) + 1))):
                    m = m // 10
                else:
                    return False
            return True
        else:
            return False
    prime_list = [i for i in range(3, x) if is_left_truncatable_prime(i)]
    return sorted(prime_list, reverse=True)