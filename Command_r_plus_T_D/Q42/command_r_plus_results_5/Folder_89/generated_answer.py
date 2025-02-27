def prime_factors(numbers_list):

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    prime_set = set()
    num = numbers_list[18]
    for i in range(2, num + 1):
        while num % i == 0:
            if is_prime(i):
                prime_set.add(i)
                num = num / i
                if num == 1:
                    break
    return prime_set