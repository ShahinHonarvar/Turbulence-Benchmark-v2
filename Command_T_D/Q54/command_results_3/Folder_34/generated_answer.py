import re
import sys

def all_right_truncatable_prime(n):
    for num in range(2, int(str(n)[-1]) + 1):
        if is_right_truncatable_prime(num):
            yield num
    return

def is_right_truncatable_prime(num):
    if num == 2 or num == 3 or num == 5 or (num == 7) or (num == 11) or (num == 13) or (num == 17):
        return True
    if num < 2 or num % 2 == 0 or num % 3 == 0 or (num % 5 == 0) or (num % 7 == 0) or (num % 11 == 0) or (num % 13 == 0) or (num % 17 == 0):
        return False
    return True