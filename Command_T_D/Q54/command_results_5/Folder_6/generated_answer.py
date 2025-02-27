import re

def all_right_truncatable_prime(nums):
    return sorted(filter(lambda x: is_right_truncatable_prime(str(x)), nums))

def is_right_truncatable_prime(s):
    if not re.fullmatch('[2-9][\\d]0+', s):
        return False
    if s[0] == '9':
        if not s[1] == '0' or not s[2:]:
            return False
    if s[0] == '8':
        return True
    if s[0] != '9':
        if not s[1] == '0' or not s[2:]:
            return False
    return True