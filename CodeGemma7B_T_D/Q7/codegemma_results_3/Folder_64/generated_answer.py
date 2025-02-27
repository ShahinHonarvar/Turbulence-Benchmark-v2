def all_even_ints_inclusive(num_list):
    """
            Returns list of even numbers from index 0 to index 4, inclusive.
            """
    even_nums = []
    for num in num_list[0:5]:
        if num % 2 == 0:
            even_nums.append(num)
    return even_nums