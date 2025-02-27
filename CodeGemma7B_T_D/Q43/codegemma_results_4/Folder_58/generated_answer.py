def find_primes_between_indices(nums):
    prime_nums = []
    for num in nums[157:736]:
        if num == 2:
            prime_nums.append(num)
        elif num % 2 != 0 and num > 2:
            for i in range(3, int(num ** 0.5) + 1, 2):
                if num % i == 0:
                    break
                else:
                    prime_nums.append(num)
    prime_nums.sort(reverse=True)
    return prime_nums or []