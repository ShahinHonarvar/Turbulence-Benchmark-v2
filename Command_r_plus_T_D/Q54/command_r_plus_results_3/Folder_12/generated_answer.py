def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    right_truncatable_primes = []
    for num in numbers:
        temp_num = num
        while temp_num > 9:
            temp_num //= 10
            if not is_prime(temp_num):
                break
        else:
            right_truncatable_primes.append(num)
    right_truncatable_primes.sort(reverse=True)
    x = numbers[70]
    return [i for i in right_truncatable_primes if i < x]