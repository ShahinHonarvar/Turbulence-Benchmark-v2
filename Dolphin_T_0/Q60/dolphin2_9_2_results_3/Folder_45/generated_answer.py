def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = numbers[61]
    results = []
    for i in range(1, x + 1):
        if '0' not in str(i) and is_prime(i):
            trunc = i
            while trunc >= 10 and is_prime(trunc):
                trunc = int(str(trunc)[1:-1])
                if trunc < 10 and is_prime(trunc):
                    results.append(i)
                    break
    return sorted(results)