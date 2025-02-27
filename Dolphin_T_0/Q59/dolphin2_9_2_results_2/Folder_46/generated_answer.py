def all_left_truncatable_prime(num_tuple):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = num_tuple[33]
    result = []
    for i in range(2, x):
        if is_prime(i) and '0' not in str(i):
            for j in range(len(str(i)) - 1, 0, -1):
                if not is_prime(int(str(i)[j:])):
                    break
            else:
                result.append(i)
    return sorted(result)