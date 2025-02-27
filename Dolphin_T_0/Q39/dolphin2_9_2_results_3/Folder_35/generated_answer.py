def return_n_greatest_chars(s):
    return sorted([i for i in s if i.isalpha()], reverse=True)[:7]