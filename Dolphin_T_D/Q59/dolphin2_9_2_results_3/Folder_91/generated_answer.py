def all_left_truncatable_prime(x):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    prime = []
    for i in range(2, x):
        if is_prime(i):
            j = i
            while j > 0 and is_prime(j):
                j = j // 10
            if j == 0:
                prime.append(i)
    prime.sort(reverse=True)
    return prime