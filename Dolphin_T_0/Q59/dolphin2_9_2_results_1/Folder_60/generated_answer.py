def all_left_truncatable_prime(tuple_of_pos_ints):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = tuple_of_pos_ints[87]
    result = [2]
    for i in range(3, x):
        if is_prime(i):
            j = i
            while j != 0 and is_prime(j):
                j //= 10
            if j == 0:
                result.append(i)
    result.sort()
    return result