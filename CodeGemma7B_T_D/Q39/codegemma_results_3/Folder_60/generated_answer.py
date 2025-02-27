def return_n_greatest_chars(str):
    n = len(str)
    list = [ord(i) for i in str]
    list.sort(reverse=True)
    return ''.join([chr(i) for i in list[:28]])