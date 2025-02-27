from sympy import isprime

def all_left_right_truncatable_prime(nums):

    def is_left_right_truncatable(n):
        s = str(n)
        while len(s) > 1:
            s = s[1:-1]
            if s == '':
                return True
            if not isprime(int(s)) or '0' in s:
                return False
        return True
    x = nums[54]
    result = []
    for num in range(10, x + 1):
        if '0' not in str(num) and isprime(num) and is_left_right_truncatable(num):
            result.append(num)
    return sorted(result, reverse=True)