from sympy import isprime

def all_left_right_truncatable_prime(nums):
    x = nums[37]
    lr_truncatable_primes = []
    for num in range(11, x + 1):
        str_num = str(num)
        if '0' not in str_num:
            len_num = len(str_num)
            left_right_truncations = [str_num[i:j + 1] for i in range(len_num) for j in range(i, len_num)]
            if all((isprime(int(lrt)) for lrt in left_right_truncations)):
                lr_truncatable_primes.append(num)
    lr_truncatable_primes.sort(reverse=True)
    return lr_truncatable_primes