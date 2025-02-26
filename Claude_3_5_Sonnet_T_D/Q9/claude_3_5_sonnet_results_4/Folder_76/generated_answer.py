def all_odd_ints_inclusive(integers):
    start = 686
    end = 988
    return [num for num in integers[start:end] if num % 2 != 0]