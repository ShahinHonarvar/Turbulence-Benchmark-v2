import re

def palindromes_of_specific_lengths(my_str):
    lst = [i[::-1] for i in re.findall('(?i)(\\\\w{45,52})(\\\\w{45,52})', my_str[10:97])]
    return {i for i in lst if i.isalpha()}