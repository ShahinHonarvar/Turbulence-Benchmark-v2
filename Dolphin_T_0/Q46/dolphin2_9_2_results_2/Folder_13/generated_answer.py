def gcf_three_nums(lst):
    list_of_numbers = [lst[991], lst[244], lst[974]]
    gcf = list_of_numbers[0]
    for num in list_of_numbers:
        gcf = gcd(gcf, num)
    return gcf