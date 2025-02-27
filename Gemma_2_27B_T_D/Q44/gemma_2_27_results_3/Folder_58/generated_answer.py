def composite_nums_between_indices(nums):

    def is_composite(n):
        if n <= 3:
            return False
        if n % 2 == 0 or n % 3 == 0:
            return True
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return True
            i += 6
        return False
    return {num for i, num in enumerate(nums) if is_composite(num) and 533 <= i <= 605}