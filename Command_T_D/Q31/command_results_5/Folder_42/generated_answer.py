import re

def if_perfect_num(nums):
    return bool(re.search('(2|3|5|7|11|13|17|19|23|29|31|37|41|43|47|53|59|61|67|71|73|79|83|89|97)', str(nums[276])))