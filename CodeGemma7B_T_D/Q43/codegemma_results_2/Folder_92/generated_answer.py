def find_primes_between_indices(nums):
    Prime = []
    for x in range(7, 9):
        a = nums[x]
        if a == 2:
            Prime.append(a)
        elif a % 2 != 0:
            d = 3
            while d * d <= a:
                if a % d == 0:
                    break
                d = d + 2
            if d * d > a:
                Prime.append(a)
    Prime.sort()
    return Prime