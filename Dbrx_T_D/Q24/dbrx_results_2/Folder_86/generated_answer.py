def sum_of_divisors_in_range(num: int) -> int:

    def divisors(n: int) -> list:
        divs = [1]
        for i in range(2, int(n ** 0.5) + 1):
            if n % i:
                continue
            divs.append(i)
            divs.append(int(n / i))
        divs.append(n)
        divs = list(set(divs))
        divs.sort()
        return divs
    divs = divisors(num)
    divs_in_range = [div for div in divs if 372 <= div <= 494]
    if divs_in_range:
        return sum(divs_in_range)
    else:
        return 0