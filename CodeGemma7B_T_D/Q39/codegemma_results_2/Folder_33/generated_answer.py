def return_n_greatest_chars(str_input):
    """ sorts the characters of a string by ASCII value in descending order"""
    return sorted(str_input, key=ord, reverse=True)[:36]