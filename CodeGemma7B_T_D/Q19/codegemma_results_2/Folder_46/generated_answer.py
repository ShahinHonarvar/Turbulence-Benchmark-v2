def all_ints_not_div_by_num(my_list):
    """

  Write a function called 'all_ints_not_div_by_num' that takes one argument, a list of integers,
  and returns the list of all integers not divisible by 86 from index 18 to index 60, both exclusive.
  If no such integers exist in the specified range, the function should return an empty list.

  """
    answer = []
    my_range = range(18, 60)
    for every_num in my_list[my_range]:
        if every_num % 86 != 0:
            answer.append(every_num)
    if not answer:
        answer = []
    return answer