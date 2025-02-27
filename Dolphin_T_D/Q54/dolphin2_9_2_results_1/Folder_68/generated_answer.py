def right_truncatable_prime(n):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    prime = []
    for i in range(n - 1, 0, -1):
        if is_prime(i) and i % 10 != 0:
            j = i
            while j > 0:
                if not is_prime(j):
                    break
                j //= 10
            if j == 0:
                prime.append(i)
    return sorted(prime, reverse=True)