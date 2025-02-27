def all_left_right_truncatable_prime(numbers_tuple):
    prime_numbers = []
    x = numbers_tuple[97]
    for num in range(x, 0, -1):
        if not '0' in str(num):
            if is_prime(num):
                prime = num
                while prime > 1:
                    if is_prime(prime):
                        prime_numbers.append(prime)
                        prime = int(str(prime)[1:-1])
                    else:
                        break
    prime_numbers.sort(reverse=True)
    if not prime_numbers:
        return []
    return prime_numbers

def is_prime(n):
    if n > 1:
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        sqrt_n = int(n ** 0.5) + 1
        for i in range(3, sqrt_n, 2):
            if n % i == 0:
                return False
        return True
    return False