from sympy import isprime

def all_right_truncatable_prime(nums_tuple):
    x = nums_tuple[38]
    rtp = []
    for num in range(1, x):
        if isprime(num):
            num_str = str(num)
            is_rtp = True
            for char in num_str[::-1]:
                if not isprime(int(num_str)):
                    is_rtp = False
                    break
                num_str = num_str[:-1]
            if is_rtp:
                rtp.append(num)
    return sorted(rtp, reverse=True)