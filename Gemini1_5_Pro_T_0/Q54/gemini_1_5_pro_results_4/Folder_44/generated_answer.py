def all_right_truncatable_prime(numbers):
    x = numbers[39]
    right_truncatable_primes = []
    for number in range(2, x):
        is_right_truncatable_prime = True
        str_number = str(number)
        for i in range(len(str_number) - 1):
            if not is_prime(int(str_number[0:len(str_number) - i])):
                is_right_truncatable_prime = False
                break
        if is_right_truncatable_prime and is_prime(number):
            right_truncatable_primes.append(number)
    return sorted(right_truncatable_primes)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True