def find_primes_between_indices(nums):
    prime_nums = []
    for i in range(229, 851):
        num = nums[i]
        if num > 1:
            for j in range(2, int(num ** 0.5) + 1):
                if num % j == 0:
                    break
            else:
                prime_nums.append(num)
    prime_nums.sort(reverse=True)
    return prime_nums if prime_nums else []