def all_left_truncatable_prime(nums):
    left_truncatable_prime = []
    for num in nums:
        if not '0' in str(num):
            prime = True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    prime = False
                    break
            if prime:
                left_truncatable_prime.append(num)
    left_truncatable_prime.sort(reverse=True)
    return left_truncatable_prime