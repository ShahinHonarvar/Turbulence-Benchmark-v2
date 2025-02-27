def all_right_truncatable_prime(nums):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def get_right_truncatable_primes(max_value):
        primes = set()
        stack = [2, 3, 5, 7]
        while stack:
            prime = stack.pop()
            if prime < max_value:
                primes.add(prime)
                for digit in range(1, 10):
                    candidate = 10 * prime + digit
                    if is_prime(candidate):
                        stack.append(candidate)
        return primes
    if len(nums) <= 70:
        return []
    x = nums[70]
    rivet = get_right_truncatable_primes(x)
    return sorted(rivet, reverse=True)