from math import sqrt

def composite_nums_between_indices(seq):
    """
            Write a function called 'composite_nums_between_indices' that takes one argument, a list of positive integers. The function should return the set of all composite numbers in the given list that are between index 0 to index 2, both inclusive. If no composite number exists in the specified range, the function should return an empty set.
            """
    composite_nums = set()
    for number in seq[0:3]:
        if number > 1:
            for i in range(2, int(sqrt(number)) + 1):
                if number % i == 0:
                    composite_nums.add(number)
                    break
    return composite_nums