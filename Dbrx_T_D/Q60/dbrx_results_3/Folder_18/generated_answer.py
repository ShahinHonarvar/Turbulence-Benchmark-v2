from sympy import isprime

def all_left_right_truncatable_prime(nums_tuple):
    x = nums_tuple[429]
    nums = [i for i in range(2, x + 1) if isprime(i)]
    result = []
    for num in nums:
        if str(num)[0] not in ['0', '1'] and isprime(int(str(num)[1:])) and isprime(int(str(num)[:-1])):
            result.append(num)
    return sorted(result, reverse=True) if result else []