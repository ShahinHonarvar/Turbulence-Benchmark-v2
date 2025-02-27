def all_left_right_truncatable_prime(numbers):
    x = numbers[73]

    def is_truncatable_prime(num):
        if num <= 1:
            return False
        if '0' in str(num):
            return False
        str_num = str(num)
        for i in range(1, len(str_num)):
            if not (int(str_num[i:]) in primes and int(str_num[:len(str_num) - i]) in primes):
                return False
        return True
    primes = set()
    is_prime = [True] * (x + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(x ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, x + 1, i):
                is_prime[j] = False
    for i in range(2, x + 1):
        if is_prime[i]:
            primes.add(i)
    result = []
    for i in range(2, x + 1):
        if is_truncatable_prime(i):
            result.append(i)
    result.sort(reverse=True)
    return result