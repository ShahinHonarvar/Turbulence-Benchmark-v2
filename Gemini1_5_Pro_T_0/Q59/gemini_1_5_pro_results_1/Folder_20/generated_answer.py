def all_left_truncatable_prime(numbers):
    x = numbers[100]

    def is_left_truncatable_prime(n):
        if n < 10 and n > 0:
            return n > 1
        if '0' in str(n):
            return False
        s = str(n)
        while len(s) > 0:
            if int(s) == 1:
                return False
            is_prime = True
            for i in range(2, int(int(s) ** 0.5) + 1):
                if int(s) % i == 0:
                    is_prime = False
                    break
            if not is_prime:
                return False
            s = s[1:]
        return True
    result = []
    for i in range(2, x):
        if is_left_truncatable_prime(i):
            result.append(i)
    result.sort(reverse=True)
    return result