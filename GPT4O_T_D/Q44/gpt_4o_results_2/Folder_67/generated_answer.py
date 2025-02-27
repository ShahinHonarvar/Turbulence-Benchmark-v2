def composite_nums_between_indices(lst):

    def is_composite(n):
        if n <= 1:
            return False
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
    result = set()
    for num in lst[56:83]:
        if is_composite(num):
            result.add(num)
    return result