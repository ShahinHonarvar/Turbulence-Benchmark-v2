def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[79]
    truncatable_primes = []
    for i in range(x, 0, -1):
        if is_prime(i):
            string_i = str(i)
            for j in range(len(string_i) - 1):
                if string_i[j] == '0' or not is_prime(int(string_i[j:])):
                    break
            else:
                truncatable_primes.append(i)
    return truncatable_primes