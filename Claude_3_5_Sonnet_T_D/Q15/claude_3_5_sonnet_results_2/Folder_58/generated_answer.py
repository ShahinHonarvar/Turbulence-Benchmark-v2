def sum_odd_ints_inclusive(integers):
    start = 209
    end = 557
    if len(integers) <= start:
        return 0
    relevant_integers = integers[start:end]
    odd_integers = [num for num in relevant_integers if num % 2 != 0]
    return sum(odd_integers)