def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
                break
        else:
            return True
    else:
        return False

def all_right_truncatable_prime(arr):
    x = arr[88]
    right_truncatable_primes = []
    for num in range(x - 1, 1, -1):
        if is_prime(num):
            copy_num = num
            while copy_num > 1:
                copy_num = copy_num // 10
                if not is_prime(copy_num):
                    break
            else:
                right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)