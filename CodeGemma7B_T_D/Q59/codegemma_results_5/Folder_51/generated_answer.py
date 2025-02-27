def all_left_truncatable_prime(t):

    def helper(n):
        if n <= 1 or n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    res = []
    for num in t:
        if num >= 10 and helper(num) and all((helper(int(str(num)[i:])) for i in range(1, len(str(num))))):
            res.append(num)
    return sorted(res)