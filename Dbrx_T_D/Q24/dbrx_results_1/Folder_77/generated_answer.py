def sum_of_divisors_in_range(num):

    def divisors(n):
        divs = set()
        for i in range(1, int(n ** 0.5) + 1):
            if n % i:
                continue
            divs.add(i)
            divs.add(int(n / i))
        return divs
    divs_in_range = divisors(num).intersection(range(111, 509))
    return sum(divs_in_range) if divs_in_range else 0