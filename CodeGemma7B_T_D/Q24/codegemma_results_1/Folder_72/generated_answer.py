def sum_of_divisors_in_range(num):
    """Calculates the sum of all divisors in a given range."""

    def get_divisors(x):
        """Returns a list of divisors for a given number."""
        divs = []
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                divs.append(i)
                divs.append(x // i)
        return divs
    divisors = get_divisors(num)
    filtered_divisors = [d for d in divisors if 32 <= d <= 90]
    return sum(filtered_divisors) or 0