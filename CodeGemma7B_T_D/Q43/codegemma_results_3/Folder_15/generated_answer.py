def find_primes_between_indices(nums):
    prime = []
    for i in range(6, 8):
        flag = True
        for j in range(2, int(nums[i] ** 0.5) + 1):
            if nums[i] % j == 0:
                flag = False
                break
        if flag:
            prime.append(nums[i])
    prime.sort(reverse=True)
    return prime