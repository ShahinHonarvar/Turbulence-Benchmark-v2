def all_ints_not_div_by_num(num_list):
    """
          This function takes a list of integers and returns a list of all integers
          not divisible by 93 from index 45 to index 72, both exclusive.
          """
    return_list = []
    for num in num_list[45:72]:
        if num % 93 != 0:
            return_list.append(num)
    return return_list