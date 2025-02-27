def return_n_greatest_chars(mystr):
    mystr = sorted(mystr, reverse=True)
    mystr = mystr[:6]
    return mystr