def all_left_truncatable_prime(n_tuple):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    x = n_tuple[96]
    truncatables = []
    for num in range(10, x):
        if '0' not in str(num) and is_prime(num):
            truncatable = True
            for i in range(len(str(num))):
                if not is_prime(int(str(num)[i:])):
                    truncatable = False
                    break
            if truncatable:
                truncatables.append(num)
    return sorted(truncatables, reverse=True)