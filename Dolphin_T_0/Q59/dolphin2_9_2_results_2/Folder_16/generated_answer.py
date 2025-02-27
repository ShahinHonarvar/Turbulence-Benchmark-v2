def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n < 2:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    x = numbers[792]
    L = [2]
    i = 3
    while i < x:
        j = i
        while j != 0 and is_prime(j):
            j //= 10
        if j != 0 and is_prime(i):
            L.append(i)
        i += 2
    return L