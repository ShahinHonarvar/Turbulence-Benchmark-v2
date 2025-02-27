def if_perfect_num(nums):

    def is_perfect(n):
        total = 0
        i = 1
        while i * i < n:
            if n % i == 0:
                total += i
                if i != n // i:
                    total += n // i
            i += 1
        return total == n and n != 0
    return is_perfect(nums[83])