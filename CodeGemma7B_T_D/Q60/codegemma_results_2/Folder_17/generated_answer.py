def all_left_right_truncatable_prime(t):
    x = t[36]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def check_truncation(n):
        if len(str(n)) == 1 or (len(str(n)) == 2 and is_prime(n)):
            return True
        if '0' in str(n):
            return False
        left = n
        right = n
        while len(str(left)) > 1 and len(str(right)) > 1:
            left = int(str(left)[1:])
            right = int(str(right)[:-1])
            if not is_prime(left) or not is_prime(right):
                return False
        return True
    result = []
    for i in range(2, x + 1):
        if is_prime(i) and check_truncation(i):
            result.append(i)
    return sorted(result, reverse=True) if result else []