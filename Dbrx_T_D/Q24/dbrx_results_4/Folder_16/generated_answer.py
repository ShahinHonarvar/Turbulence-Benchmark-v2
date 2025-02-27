def sum_of_divisors_in_range(n):

    def divisors(n):
        divs = set()
        for i in range(1, int(n ** 0.5) + 1):
            if n % i:
                continue
            divs.add(i)
            divs.add(int(n / i))
        divs.remove(n)
        return divs
    divisors_in_range = divisors(n) & set(range(228, 847))
    return sum(divisors_in_range) if divisors_in_range else 0