def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[36]
    left_right_truncatable_primes = []
    for num in range(2, x + 1):
        str_num = str(num)
        if '0' not in str_num:
            is_left_right_truncatable_prime = True
            left = 0
            right = len(str_num) - 1
            while left < right:
                if not is_prime(int(str_num[left:right + 1])):
                    is_left_right_truncatable_prime = False
                    break
                left += 1
                right -= 1
            if is_left_right_truncatable_prime:
                left_right_truncatable_primes.append(num)
    return sorted(left_right_truncatable_primes, reverse=True)