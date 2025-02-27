import re

def return_n_greatest_chars(str_input):
    return re.findall('[A-Z]', str_input)[-36:]