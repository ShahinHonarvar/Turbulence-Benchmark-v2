def all_left_truncatable_prime(vals):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = vals[71]
    results = [i for i in range(2, x) if is_prime(i) and (not '0' in str(i)) and all((int(str(i)[j:]) for j in range(1, len(str(i)))))]
    return sorted(results, reverse=True)