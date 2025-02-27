def find_primes_between_indices(nums):
    result = []
    for num in nums[19:91]:
        prime = True
        if num <= 1:
            prime = False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                prime = False
        if prime:
            result.append(num)
    result.sort(reverse=True)
    return result if result else []