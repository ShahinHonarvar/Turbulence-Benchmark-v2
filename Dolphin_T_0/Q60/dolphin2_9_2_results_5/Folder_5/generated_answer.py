def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n in (2, 3):
            return True
        if n < 2 or n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True
    x = numbers[55]
    result = []
    for i in range(2, x + 1):
        if i < 10:
            if is_prime(i):
                result.append(i)
        elif i % 10 != 0 and is_prime(i):
            prime = True
            while i > 9 and prime:
                if i % 10 == 0:
                    prime = False
                elif not is_prime(int(str(i)[1:-1] if len(str(i)) > 2 else str(i)[1:])):
                    prime = False
                else:
                    i //= 10
            if prime:
                result.append(i)
    return sorted(result)