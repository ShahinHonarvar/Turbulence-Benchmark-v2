def all_left_truncatable_prime(arr):
    x = arr[89]
    result = []

    def prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for i in range(2, x):
        if not str(i).startswith('0') and prime(i):
            temp = i
            while temp != 0:
                if not prime(temp):
                    break
                temp //= 10
            else:
                result.append(i)
    return sorted(result)[::-1]