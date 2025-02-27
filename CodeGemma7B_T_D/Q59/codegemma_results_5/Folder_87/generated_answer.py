def all_left_truncatable_prime(nums):
    result = []
    for n in nums:
        if n % 2 == 0:
            continue
        factors = [i for i in range(3, int(n ** 0.5) + 1, 2) if n % i == 0]
        if not factors:
            temp = str(n)
            if temp.count('0') == 0:
                result.append(n)
    return sorted(result, reverse=True)