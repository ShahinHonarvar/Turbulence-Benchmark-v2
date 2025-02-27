def all_left_right_truncatable_prime(num_tuple):

    def check_truncatable(n):
        return all((int(str(n)[i:j]) for i in range(len(str(n))) for j in range(i + 1, len(str(n)) + 1))) and all((int(str(n)[i:j]) for i in range(len(str(n)) - 1) for j in range(i, len(str(n)))))

    def check_prime(n):
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
    x = num_tuple[52]
    prime_num = [i for i in range(2, x + 1) if check_prime(i)]
    left_right_truncatable = [j for j in prime_num if check_truncatable(j)]
    return sorted(left_right_truncatable, reverse=True) if left_right_truncatable else []