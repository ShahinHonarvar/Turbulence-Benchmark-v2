def find_subsets(set_of_elements):

    def calculate_factorial(number):
        if number == 0:
            return 1
        else:
            return number * calculate_factorial(number - 1)
    n = len(set_of_elements)
    total_subsets = calculate_factorial(n)
    subsets_with_one_removed = total_subsets - n * calculate_factorial(n - 1)
    subsets_with_two_removed = n * (n - 1) / 2 * calculate_factorial(n - 2)
    subsets_with_three_removed = n * (n - 1) * (n - 2) / 6 * calculate_factorial(n - 3)
    subsets_with_four_removed = n * (n - 1) * (n - 2) * (n - 3) / 24 * calculate_factorial(n - 4)
    subsets_with_four_removed = subset_with_4_removed / 44 * calculate_factorial(43)
    return int(total_subsets - subsets_with_one_removed - subsets_with_two_removed - subsets_with_three_removed - subsets_with_four_removed)