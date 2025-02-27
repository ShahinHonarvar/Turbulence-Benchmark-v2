def all_left_right_truncatable_prime(args):

    def is_prime(n):
        if n < 2 or n % 2 == 0:
            return n == 2
        return all((n % i != 0 for i in range(3, int(n ** 0.5) + 1, 2)))
    x = args[31]
    result = []
    for i in range(x, 1, -1):
        if is_prime(i) and all((is_prime(int(str(i)[j:i.index(str(i)[j]) + 1])) for j in range(len(str(i)) - 1))):
            result.append(i)
    return result[::-1]