def all_left_right_truncatable_prime(tuples):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = tuples[69]
    truncatables = []
    for num in range(x, 1, -1):
        if (is_prime(num) and (not '0' in str(num))) and (is_prime(str(num)[1:-1]) and (not '0' in str(num)[1:-1])):
            truncatables.append(num)
    return sorted(truncatables, reverse=True)