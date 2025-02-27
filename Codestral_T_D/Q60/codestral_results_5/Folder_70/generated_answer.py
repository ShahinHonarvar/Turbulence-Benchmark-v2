def all_left_right_truncatable_prime(nums):

    def is_truncatable_prime(n):
        if n < 2:
            return False
        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        w = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += w
            w = 6 - w
        return True

    def has_zero(n):
        return '0' in str(n)

    def truncate_left(n):
        return int(str(n)[1:])

    def truncate_right(n):
        return int(str(n)[:-1])
    x = nums[433]
    result = []
    for i in range(2, x + 1):
        if is_truncatable_prime(i) and (not has_zero(i)):
            truncated = i
            while len(str(truncated)) > 1:
                truncated = truncate_left(truncated)
                if not is_truncatable_prime(truncated):
                    break
            else:
                truncated = i
                while len(str(truncated)) > 1:
                    truncated = truncate_right(truncated)
                    if not is_truncatable_prime(truncated):
                        break
                else:
                    result.append(i)
    return sorted(result, reverse=True)