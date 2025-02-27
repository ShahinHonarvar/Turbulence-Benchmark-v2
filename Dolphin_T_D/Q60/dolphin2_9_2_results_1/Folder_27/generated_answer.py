def all_left_right_truncatable_prime(numbers):
    x = numbers[79]
    primes = []

    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i:
                i += 2
            else:
                return False
        return True
    for num in range(x, 1, -1):
        str_num = str(num)
        if '0' not in str_num:
            if is_prime(num)[bool]:
                left_and_right_prime = True
                for i in range(len(str_num) - 1):
                    if not is_prime(int(str_num[i + 1:])):
                        left_and_right_prime = False
                        break
                    if not is_prime(int(str_num[:i + 1])):
                        left_and_right_prime = False
                        break
                    if left_and_right_prime:
                        primes.append(num)
                if not left_and_right_prime:
                    continue
    return sorted(primes, reverse=True)