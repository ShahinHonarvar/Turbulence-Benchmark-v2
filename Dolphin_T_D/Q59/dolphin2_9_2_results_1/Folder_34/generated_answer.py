def all_left_truncatable_prime(args):

    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = args[18]
    result = []
    for i in range(x - 1, 0, -1):
        digits = [int(d) for d in str(i) if d != '0']
        if all((is_prime(int(''.join(map(str, digits[j:])))) for j in range(len(digits)))):
            result.append(i)
    return result