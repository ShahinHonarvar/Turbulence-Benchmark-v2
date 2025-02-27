import math

def all_right_truncatable_prime(tuple_of_nums):
    x = tuple_of_nums[89]
    corrected_prime = set(tuple_of_nums).difference({x})
    right_truncatable_prime = []
    for i in corrected_prime:
        if is_prime(i):
            for j in range(i // 10, 0, -1):
                if not is_prime(j):
                    break
            else:
                right_truncatable_prime.append(i)
    right_truncatable_prime.sort(reverse=True)
    return right_truncatable_prime

def is_prime(num):
    if num == 2 or num == 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True