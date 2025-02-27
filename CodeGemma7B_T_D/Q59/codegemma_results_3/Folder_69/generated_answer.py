def all_left_truncatable_prime(x):
    prime = [i for i in range(x) if all((j not in str(i) for j in '0'))]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    result = []
    for i in prime:
        if all((is_prime(int(str(i)[j:])) for j in range(1, len(str(i))))):
            result.append(i)
    result.sort(reverse=True)
    return result